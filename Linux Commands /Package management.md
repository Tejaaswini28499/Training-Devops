## Package Management
```
1. APT (Advanced Package Tool) – Debian/Ubuntu-based Systems
  
  APT is the package manager used in Debian and Ubuntu-based distributions like Linux Mint and Pop!_OS. It works with .deb packages and automatically resolves dependencies.

eg: sudo apt update , sudo apt install package_name

2. YUM/DNF – Red Hat/CentOS/Fedora-based Systems
    
    YUM and DNF are package managers used on Red Hat, CentOS, and Fedora distributions. YUM is older, and DNF is a newer version designed to improve performance and dependency management. They handle .rpm packages.

eg: sudo dnf upgrade , sudo dnf install package_name

3. dpkg – Low-Level Tool for Debian/Ubuntu-based Systems
    
    dpkg is the low-level package manager used by APT to handle .deb packages. It can be used directly but does not handle dependencies like APT.
 
eg:sudo dpkg -i package_name.deb
```


