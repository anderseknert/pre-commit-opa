from setuptools import setup

setup(
    name='pre-commit-opa',
    description='Pre-commit hooks for Open Policy Agent and Rego policies',
    url='https://github.com/anderseknert/pre-commit-opa',
    version_format='{tag}+{gitsha}',

    author='Anders Eknert',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=[
        'pre_commit_hooks',
    ],

    install_requires=[
        'setuptools-git-version',
    ],

    scripts=[
        'pre_commit_hooks/opa-check.py',
        'pre_commit_hooks/opa-eval.py',
        'pre_commit_hooks/opa-fmt.py',
        'pre_commit_hooks/opa-test.py',
    ]
)