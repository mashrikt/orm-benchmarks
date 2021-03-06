import os
import time

from models import Journal, engine
from sqlalchemy.orm import sessionmaker

count = int(os.environ.get('ITERATIONS', '1000'))


Session = sessionmaker(bind=engine)

start = time.time()
session = Session()
count = 0

for _ in range(10):
    for level in ['A', 'B', 'C']:
        res = list(session.query(Journal).filter(Journal.text.contains(f'from {level},')))
        count += len(res)

now = time.time()

print(f'SQLAlchemy ORM, E: Rows/sec: {count / (now - start): 10.2f}')
