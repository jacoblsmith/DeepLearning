## Setting up an Amazon Image for computing with the Theano

Choose Ubuntu 12.04 HVM Image

Login 

    ssh -i YOUR.pem ubuntu@ec2-##-##-##-##.compute-1.amazonaws.com

Update your installation and install necessary software
    
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install python-numpy python-scipy python-dev python-pip python-nose g++ libopenblas-dev git unzip

Make a directory to save all your software downloads and download 64 bit [Anaconda](http://continuum.io/downloads) and CUDA 5.5 software [.deb for Ubuntu 12.04](https://developer.nvidia.com/cuda-downloads)
    
    mkdir software
    cd software
    wget http://SOME URL/Anaconda-1.7.0-Linux-x86_64.sh
    wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1204/x86_64/cuda-repo-ubuntu1204_5.5-0_amd64.deb

Install CUDA
    
    sudo dpkg -i cuda-repo-ubuntu1204_5.5-0_amd64.deb
    sudo apt-get update
    sudo apt-get install cuda

Append your path, edit your .bashrc file and add the following at the end
    
    PATH=/usr/local/cuda/bin:$PATH
    LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH


Install Anaconda, I stuck with the install in my home directory and had the script modify my environment
    
    bash Anaconda-<versioin>.sh
    bash ~/.bashrc
    
Check that you are using the right python
        
    python --version
    
Update Anaconda and install MKL
    
    conda update conda
    conda update anaconda
    conda install mkl
    
    
Download Theano and install Theano

    git clone git://github.com/Theano/Theano.git
    cd Theano
    python setup.py install
    
Test your Theano install

    THEANO_FLAGS=floatX=float32,device=gpu python ~/anaconda/lib/python2.7/site-packages/theano/misc/check_blas.py
    THEANO_FLAGS=floatX=float32,device=cpu python ~/anaconda/lib/python2.7/site-packages/theano/misc/check_blas.py
    

Set the GPU as your default insert the following in ~/.theanorc

    [global]
    floatX = float32
    device = gpu0
    
    [nvcc]
    fastmath = True## Setting up an Amazon Image for computing with the Theano