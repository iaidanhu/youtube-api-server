import time
from typing import Any, Optional

from app.core.config import settings


class MemoryCache:
    """
    简单的内存缓存类，带TTL（Time To Live）机制
    """
    def __init__(self, default_ttl: int = None):  # 默认1小时
        """
        初始化缓存
        
        Args:
            default_ttl: 默认过期时间（秒）
        """
        self._cache = {}
        self._default_ttl = default_ttl or settings.CACHE_DEFAULT_TTL  # 默认1小时

    def _is_expired(self, timestamp: float) -> bool:
        """
        检查缓存项是否已过期
        
        Args:
            timestamp: 缓存项的时间戳
            
        Returns:
            bool: 如果已过期返回True，否则返回False
        """
        return time.time() - timestamp > self._default_ttl

    def get(self, key: str) -> Optional[Any]:
        """
        从缓存中获取数据
        
        Args:
            key: 缓存键
            
        Returns:
            缓存的数据，如果不存在或已过期则返回None
        """
        if key in self._cache:
            data, timestamp = self._cache[key]
            if not self._is_expired(timestamp):
                return data
            else:
                # 删除已过期的缓存项
                del self._cache[key]
        return None

    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        """
        将数据存储到缓存
        
        Args:
            key: 缓存键
            value: 要缓存的数据
            ttl: 过期时间（秒），如果为None则使用默认值
        """
        ttl = ttl or self._default_ttl
        self._cache[key] = (value, time.time() + ttl - self._default_ttl)

    def delete(self, key: str) -> bool:
        """
        删除缓存项
        
        Args:
            key: 要删除的缓存键
            
        Returns:
            bool: 如果成功删除返回True，否则返回False
        """
        if key in self._cache:
            del self._cache[key]
            return True
        return False

    def clear(self) -> None:
        """
        清空所有缓存
        """
        self._cache.clear()

    def cleanup_expired(self) -> None:
        """
        清理所有已过期的缓存项
        """
        expired_keys = []
        current_time = time.time()
        
        for key, (data, timestamp) in self._cache.items():
            if current_time - timestamp > self._default_ttl:
                expired_keys.append(key)
        
        for key in expired_keys:
            del self._cache[key]

    def size(self) -> int:
        """
        获取缓存中当前项的数量
        
        Returns:
            int: 缓存项的数量
        """
        # 清理过期项后再计算大小
        self.cleanup_expired()
        return len(self._cache)


# 创建全局缓存实例
cache = MemoryCache()