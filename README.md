[![Travis](https://img.shields.io/travis/mmckinst/mg-travis-ci.svg)](https://travis-ci.org/mmckinst/mg-travis-ci)

This RPM gets built every time I push to the repo. The repo and final RPM are on
copr at
[marknexcess/mg](https://copr.fedorainfracloud.org/coprs/marknexcess/mg/).

With
[.travis.yaml](https://github.com/mmckinst/mg-travis-ci/blob/master/.travis.yml)
it installs rpm, wget, and copr-cli in Travis's environment. Travis then runs a
command to download the source tarball from the spec file, builds the src.rpm,
and submits it to copr using copr-cli. The credentials for this are encrypted in
the repo at
[.copr.enc](https://github.com/mmckinst/mg-travis-ci/blob/master/.copr.enc) and
decrypted by Travis.

Travis runs Ubuntu but it doesn't matter because it just builds the src.rpm,
which is simple to do, and submits that to copr.

Caveats
---

You need to make sure you bump the release number when you commit if you want
copr to actually build it. If you submit something with the same version number
[it won't build](https://fedorahosted.org/copr/wiki/UserDocs#WhathappenswhenItrytobuildapackagewiththesameversionnumber).
