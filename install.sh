#!/bin/bash 

sourceCommand = ""

env=$(hostname)

OS=$(hostnamectl | grep "CPE OS Name")
echo $OS

if [ -z "$1" ]; then 
    if [[ "$OS" == *"centos:7"* ]]; then
        echo centos7
        sourceCommand="$sourceCommand""; source /cvmfs/sft.cern.ch/lcg/views/LCG_103/x86_64-centos7-gcc11-opt/setup.sh"
    elif [[ "$OS" == *"enterprise_linux:9"* ]]; then
        echo el9
        sourceCommand="$sourceCommand""; source /cvmfs/sft.cern.ch/lcg/views/LCG_103/x86_64-centos9-gcc11-opt/setup.sh"	
    else
        echo "$OS"" not supported"
    fi
else 
    sourceCommand = "export LD_LIBRARY_PATH=$(root-config --libdir):$(pwd)/xrdfs_locallib/lib:/.singularity.d/libs"
fi

eval "$sourceCommand"

python -m venv --system-site-packages myenv
source myenv/bin/activate

python -m pip install -e ".[docs,dev]"

python -m pip install --no-binary=correctionlib correctionlib

cd utils
mkdir -p bin

cd src && c++ hadd.cxx -o hadd2 $(root-config --cflags --libs) && cd .. && mv src/hadd2 bin/hadd2

if [ $? -ne 0 ]; then
    echo "Failed compiling hadd"
    exit 1
fi
cd ..



cat <<EOF > start.sh
#!/bin/bash
$sourceCommand
source `pwd`/myenv/bin/activate
export STARTPATH=`pwd`/start.sh 
export PYTHONPATH=`pwd`/myenv/lib64/python3.9/site-packages:\$PYTHONPATH
export PATH=`pwd`/utils/bin:\$PATH
EOF


chmod +x start.sh

wget https://gpizzati.web.cern.ch/mkShapesRDF/jsonpog-integration.tar.gz
tar -xzvf jsonpog-integration.tar.gz
rm -r jsonpog-integration.tar.gz
mv jsonpog-integration mkShapesRDF/processor/data/
