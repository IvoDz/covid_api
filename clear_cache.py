from flask_caching import Cache

from api import app, config


# Sample script from flask-caching documentation for cache clearing
cache = Cache()

def main():
    cache.init_app(app, config=config)

    with app.app_context():
        cache.clear()

if __name__ == '__main__':
    main()