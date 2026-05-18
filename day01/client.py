from redis import Redis

# example of redis operations
redis_cli = Redis(host='localhost', port=6379, db=0)

redis_cli.set('name', 'Alice')

name = redis_cli.get('name')

redis_cli.delete('name')