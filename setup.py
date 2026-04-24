from setuptools import setup, find_packages

setup(
    name='mariadb-synch-binlog',
    version='0.1.0',
    description='MariaDB binlog sync engine',
    packages=find_packages(include=[
        'src', 'src.*',
        'plugins_test', 'plugins_test.*',
        'config', 'config.*',
    ]),
    install_requires=[
        'pymysql',
        'mysql-replication',
        'clickhouse-connect',
    ],
    python_requires='>=3.7',
)
