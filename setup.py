from setuptools import setup, find_packages

setup(
    name='mariadb-synch-binlog',
    version='0.1.0',
    packages=find_packages(
        include=[
            'mariadb_synch_binlog',
            'mariadb_synch_binlog.src',
            'mariadb_synch_binlog.src.*',
        ],
        exclude=[
            'mariadb_synch_binlog.tests',
            'mariadb_synch_binlog.tests.*',
            'mariadb_synch_binlog.plugins_test',
            'mariadb_synch_binlog.plugins_test.*',
            'mariadb_synch_binlog.config',
            'mariadb_synch_binlog.config.*',
        ],
    ),
    install_requires=[
        'pymysql',
        'mysql-replication',
        'clickhouse-connect',
    ],
    python_requires='>=3.7',
)
