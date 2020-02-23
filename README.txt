# KFUPM-SSL Artificial Intelligence(AI) Team
The AI team is responsible for the development, and implementation of the robots AI, and logic. 
Moreover, the main goal of the team is to learn by trying, falling, mistakes, and team work; However,
the team is passionate to participate in the Robocup event with functional, and competitive robots.

## New Members
For new members take the [udacity git](https://www.udacity.com/course/version-control-with-git--ud123) course to be familier with git tool and github

## Starting


### SSL Tools


### ssl-vision


### protobuf


## grSim    
**Note**: Run these two commands sudo apt upgrade sudo apt update 

### Installation instructions
Before following the installation instructions run these two commands
```
$ sudo apt-get update
$ sudo apt-get install
```

Follow the installation instructions that are provided by the RoboCup-SSL [installation instructions](https://github.com/RoboCup-SSL/grSim/blob/master/INSTALL.md)

The RoboCup-SSL installation instructions miss installing the [Open Dynamics Engine (ODE)](www.ode.org)
Follow The Instructions to download ODE, and install it.

* Download ODE:
To download the source code for ODE we will use hg (mercurial) to clone the source code from [bitbucket.org](https://bitbucket.org)

1. Install hg (mercurial)
```
$ sudo apt install mercurial
```

2. Clone ODE at your preferred location
```
$ cd your/preferred/location
$ hg clone https://bitbucket.org/odedevs/ode
```

* Building ODE With Cmake:
ODE can be built using 5 ways for [more information](https://bitbucket.org/odedevs/ode/raw/default/INSTALL.txt)


1. Create build file at your preferred location 
```
$ cd your/preferred/location
$ mkdir ode-build
$ cd ode-build
```

2. Call CMake with the path to ODE's source directory
```
$ cmake ode/source/location
```

[source code for OPE](https://bitbucket.org/odedevs/ode/src/default)

## helpfull sources
* [Small Size League](https://ssl.robocup.org)
