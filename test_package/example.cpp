#include <iostream>
#include <QDir>
#include <QFileInfo>
#include <quazip.h>

int main() {
	QuaZip quazip;
	quazip.setZipName("quazip_test_package.zip");
	quazip.open(QuaZip::mdCreate);
	quazip.close();
	if (!QFileInfo(quazip.getZipName()).exists()) {
		std::cout << "Something went wrong: test archive has not been created\n";
	}
	else {
		std::cout << quazip.getZipName().toStdString() << " successfully created\n";
		if (QDir().remove(quazip.getZipName())) {
			std::cout << quazip.getZipName().toStdString() << " successfully removed\n";
		}
		else {
			std::cout << "Something went wrong:" << quazip.getZipName().toStdString() << " has not been removed\n";
		}
	}
}
