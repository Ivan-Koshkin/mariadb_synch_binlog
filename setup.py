from setuptools import setup

setup(
    name='mariadb-synch-binlog',
    version='0.1.2',
    description='MariaDB binlog sync engine',
    package_dir={
        'mariadb_synch_binlog': 'src',
    },
    packages=['mariadb_synch_binlog'],
    install_requires=[
        'pymysql',
        'mysql-replication',
        'clickhouse-connect',
    ],
    python_requires='>=3.7',
)
