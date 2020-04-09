## CGEM SimPEG Examples
SimPEG examples that are specific for CGEM students. The idea is that we can create notebooks here that highlight specific use cases for geophysics graduate students and then once they get cleaned up to the point of being useful, we can commit them back to the SimPEG repository.

## Getting the examples

Get the latest sample code from GitHub using Git or download the repository as a ZIP file.
([Download](https://github.com/ckohnke/cgem-simpeg-examples/archive/master.zip))

    git clone https://github.com/ckohnke/cgem-simpeg-examples.git

## Before you begin

1.  Download and install [SimPEG](https://github.com/simpeg/simpeg), in your perfered way (Anaconda + Jupyter notebooks is the preferred method by the maintainers of this repository).

2. Make sure the Python packages in requirements.txt are installed. This can be done with the command inside the directory. This can also be accomplished in a conda environment.
    
        pip install -r requirements.txt
    
## Contributing changes

* See [CONTRIBUTING.md](CONTRIBUTING.md)

## Repository Structure

Each folder is a separate geophysical method, and the Jupyter notebooks inside those folders include examples on using SimPEG for that method. Each notebook (should be) well documented and serve as both a basic tutorial and as an example for the use case. The notebooks can be run in the usual way using the [Jupyter](https://jupyter.org/) project.

Other utilities that are useful for dealing with fileIO or other  SimPEG objects will go into the utils directory. It may be useful to add this directory to your PYTHONPATH while dealing with these examples.

## Licensing

* See [LICENSE](LICENSE)

## SimPEG Links
* [Website](https://simpeg.xyz/)
* [Github](https://github.com/simpeg/simpeg)
* [Installing](https://docs.simpeg.xyz/content/basic/installing.html)
