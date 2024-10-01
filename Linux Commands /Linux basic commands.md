ls
cd
mkdir 
rm -rf - delete with file&folder
rm filename
cp sourcepath destinationpath - copy 
cp -r sourcepath destinationpath - copy all things in directory
cp -r sourcepath/* destinationpath (will copy all the files inside to new path)
cat 
touch
cd / - go to root directory
cd ~ - home path

sudo su or sudo -i = root user
su - ec2-user = back to normal user

pwd - present working directory
rm *.txt - in directory remove only .text file
rm -rf * - delete all note: don't use this command as a root user as it deletes entire system

mkdir image{1..5} - To create 5 image with naming image1, image2..image5
touch Filename{1..5}.txt - to create 5 files with "Filename1.txt , Filename2.txt... Filename5.txt"
mkdir image{1..5}_yogi - create image with imagename as "image1_yogi , image2_yogi... iamge5_yogi"
ls -l - information 
whoami = username

mkdir teju yogi = this create teju directory
mkdir teju/yogi -p = this create a tejudirectory inside that yogi subdirectory will be created 
--help = help you

mv sp dp = will move the file
mv *.txt dp = to move all .txt file to destination path

ln -s filepath linkname = Symbolic Links

cat /etc/os-release = To check OS infomation 

