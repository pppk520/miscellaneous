mkdir -p $GOPARDIR

cd /tmp
wget https://redirector.gvt1.com/edgedl/go/go1.9.2.linux-amd64.tar.gz
tar -xf go1.9.2.linux-amd64.tar.gz
mv go $GOPARDIR
$GOROOT/bin/go get -u github.com/gopherdata/gophernotes
mkdir -p ~/.local/share/jupyter/kernels/gophernotes
cp $GOPATH/src/github.com/gopherdata/gophernotes/kernel/* ~/.local/share/jupyter/kernels/gophernotes

