import os
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication,QMainWindow,QMessageBox,QFileDialog,QProgressBar
from ui_comp import Ui_Form
import zipfile, tarfile, gzip


class mainWindow (QMainWindow,Ui_Form):
    def __init__(self,app):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Compressor/Decompressor Software")

        self.app = app

        self.file_selec.clicked.connect(self.select_file_or_folder)
        self.format_combo.addItems(["zip","tar","gzip"])

        self.compress.clicked.connect(self.compress_file_or_folder)
        self.file_selec2.clicked.connect(self.select_file_or_folder_to_decomp)

        self.progress_bar = QProgressBar(self)
        self.statusBar().addWidget(self.progress_bar)

        self.decompress.clicked.connect(self.decompressed)

    def select_file_or_folder(self):
        options = QFileDialog.Options()
        self.file_or_folder_path, _ = QFileDialog.getOpenFileName(self, "Select File or Folder", "", 
                                                                  "All Files (*);;Folder (*)",
                                                                  options=options)
        if self.file_or_folder_path:
            self.label.setText(f"Selected: {self.file_or_folder_path}")


    def compress_file_or_folder(self):
        if not hasattr(self, 'file_or_folder_path') or not self.file_or_folder_path:
            QMessageBox.warning(self, "Warning", "No File or Folder Selected!")
            return
            
        format_selected = self.format_combo.currentText()
        if format_selected == "zip":
            self.compress_to_zip()
        elif format_selected == "tar":
            self.compress_to_tar()
        elif format_selected == "gzip":
            self.compress_to_gzip()

    
    def compress_to_zip(self):
        zip_file_name, _ = QFileDialog.getSaveFileName(self, "Save Compressed File",
                                                       "",
                                                       "Zip Files (*.zip)")
        zip_file_name = zip_file_name.__add__(".zip")
        if zip_file_name:
            try:
                with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                    if os.path.isdir(self.file_or_folder_path):
                        for root, files in os.walk(self.file_or_folder_path):
                            for file in files:
                                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), self.file_or_folder_path))

                    else:
                        zipf.write(self.file_or_folder_path, os.path.basename(self.file_or_folder_path))
                QMessageBox.information(self, "Success", f"Compressed file saved as: {zip_file_name}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occured:{e}")


    def compress_to_tar(self):
            tar_file_name, _ = QFileDialog.getSaveFileName(self, "Save Compressed File",
                                                        "",
                                                        "Tar Files (*.tar)")
            tar_file_name = tar_file_name.__add__(".tar")
            if tar_file_name:
                try:
                    with tarfile.open(tar_file_name, 'w') as tarf:
                        if os.path.isdir(self.file_or_folder_path):
                                    tarf.add(self.file_or_folder_path, arcname=os.path.basename(self.file_or_folder_path))

                        else:
                            tarf.add(self.file_or_folder_path, arcname=os.path.basename(self.file_or_folder_path))
                    QMessageBox.information(self, "Success", f"Compressed file saved as: {tar_file_name}")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"An error occured:{e}")

    def compress_to_gzip(self):
            gzip_file_name, _ = QFileDialog.getSaveFileName(self, "Save Compressed File",
                                                        "",
                                                        "Gzip Files (*.gz)")
            gzip_file_name = gzip_file_name.__add__(".gz")
            if gzip_file_name:
                try:
                    with open(self.file_or_folder_path, 'rb') as f_in:
                        with gzip.open(gzip_file_name, 'wb') as f_out:
                            f_out.writelines(f_in)

                    QMessageBox.information(self, "Success", f"Compressed file saved as: {gzip_file_name}")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"An error occured:{e}")


    def select_file_or_folder_to_decomp(self):
        options = QFileDialog.Options()
        self.file_path, self._ = QFileDialog.getOpenFileName(self, "Select Compressed File",
                                                    "{self.file_path}",
                                                    "Zip Files (*.zip);; Tar Files (*.tar);; Gzip Files (*.gz)",
                                                    options=options)
        if not self.file_path:
            return
        else:
            self.label_2.setText(f"Selected: {self.file_path}")
        return self.file_path, self._

    def decompressed(self):
        if  self._ == "Zip Files (*.zip)":
            self.decompress.clicked.connect(self.decompress_zip)
        if self._ == "Tar Files (*.tar)":
            self.decompress.clicked.connect(self.decompress_tar)
        if self._ == "Gzip Files (*.gz)":
            self.decompress.clicked.connect(self.decompress_gzip)

    def decompress_zip(self):
        output_dir = QFileDialog.getExistingDirectory(self, "Select Output Directory")
        if output_dir:
            try:
                with zipfile.ZipFile(self.file_path, "r") as zip_ref:
                    zip_ref.extractall(output_dir)
                QMessageBox.information(self, "Success", f"Decompressed file saved to: {output_dir}")
            except Exception as e:
                QMessageBox.critical(self, "Error",f"An Error occured: {e}")

    def decompress_tar(self):
        output_dir = QFileDialog.getExistingDirectory(self, "Select Output Directory")
        if output_dir:
            try:
                with tarfile.open(self.file_path, "r") as tar_ref:
                    tar_ref.extractall(output_dir)
                QMessageBox.information(self, "Success", f"Decompressed file saved to: {output_dir}")
            except Exception as e:
                QMessageBox.critical(self, "Error",f"An Error occured: {e}")

    def decompress_gzip(self):
        output_file, _ = QFileDialog.getSaveFileName(self, "Save Decompressed File", "",
                                                     "All Files (*.*)")
        if output_file:
            try:
                with gzip.open(self.file_path, "rb") as f_in:
                    with open(output_file, "wb") as f_out:
                        f_out.writelines(f_in)
                QMessageBox.information(self, "Success", f"Decompressed file saved as: {output_file}")
            except Exception as e:
                QMessageBox.critical(self, "Error",f"An Error occured: {e}")



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = mainWindow(app)
    window.show()
    sys.exit(app.exec())