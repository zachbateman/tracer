import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='tracer',
    version='0.0.1',
    packages=['tracer'],
    license='MIT',
    author='Zach Bateman',
    description='Python class instance insights',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/zachbateman/tracer.git',
    download_url='https://github.com/zachbateman/tracer/archive/v_0.0.1.tar.gz',
    keywords=['CLASS', 'INSTANCE', 'METACLASS'],
    install_requires=[],
    classifiers=['Development Status :: 3 - Alpha',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   ]
)
