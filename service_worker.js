// キャッシュファイルの指定
var CACHE_NAME = 'pwa-sample-caches';
var urlsToCache = [
    '/',
    '/assets/talk.js',
    '/assets/talk2.js',
    '/assets/talk3.js',
    '/assets/talk4.js',
    '/assets/talk5.js',
    '/assets/talk6.js',
    '/assets/icons/image014.png',
    '/index.html',
    '/style.css'
];
var version = "0.22";

// インストール処理
self.addEventListener('install', function(event) {
    event.waitUntil(
        caches
            .open(CACHE_NAME)
            .then(function(cache) {
                return cache.addAll(urlsToCache);
            })
    );
});

// リソースフェッチ時のキャッシュロード処理
self.addEventListener('fetch', function(event) {
    event.respondWith(
        caches
            .match(event.request)
            .then(function(response) {
                return response ? response : fetch(event.request);
            })
    );
});