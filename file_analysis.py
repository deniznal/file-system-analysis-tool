import os
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
from pathlib import Path

class FileSystemAnalyzer:
    def __init__(self):
        self.file_sizes = []
        self.file_types = defaultdict(int)
        self.other_types = defaultdict(int)
        self.size_ranges = {
            '1KB': 1024,
            '10KB': 10 * 1024,
            '100KB': 100 * 1024,
            '1MB': 1024 * 1024,
            '10MB': 10 * 1024 * 1024,
            '100MB': 100 * 1024 * 1024,
            '1GB': 1024 * 1024 * 1024,
            '10GB': 10 * 1024 * 1024 * 1024
        }
        
    def get_file_type_category(self, extension):
        categories = {
            'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', 
                         '.ppt', '.pptx', '.md', '.csv', '.json', '.xml', '.yaml', '.yml',
                         '.epub', '.mobi', '.azw', '.azw3', '.lit', '.fb2', '.djvu', '.msg',
                         '.properties', '.xsd', '.resx', '.info', '.adoc', '.po', '.rdb'],
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp', 
                      '.ico', '.psd', '.ai', '.eps', '.raw', '.cr2', '.nef', '.heic', '.heif',
                      '.tga', '.exr', '.hdr', '.indd', '.ind', '.cdr', '.dds', '.wmf', '.cur',
                      '.fon', '.bcmap'],
            'Videos': ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.webm', '.m4v', 
                      '.3gp', '.mpeg', '.mpg', '.ts', '.mts', '.m2ts', '.vob', '.ogv',
                      '.mxf', '.m2v', '.m4v', '.svi', '.3g2', '.f4v', '.f4p', '.f4a', '.f4b'],
            'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a', '.wma', '.mid', 
                     '.midi', '.opus', '.aiff', '.alac', '.wv', '.ape', '.ac3', '.dts',
                     '.aac', '.mka', '.tta', '.tak', '.ofr', '.ofs', '.spx', '.hca'],
            'Code': ['.py', '.java', '.cpp', '.c', '.js', '.html', '.css', '.php', '.rb', 
                    '.go', '.rs', '.swift', '.kt', '.ts', '.jsx', '.tsx', '.vue', '.svelte',
                    '.sh', '.bash', '.zsh', '.ps1', '.bat', '.cmd', '.vbs', '.wsf', '.reg',
                    '.inf', '.ini', '.cfg', '.config', '.yml', '.yaml', '.toml', '.env',
                    '.h', '.hpp', '.cs', '.groovy', '.cmake', '.qml', '.vim', '.glsl', '.lua',
                    '.tcl', '.pri', '.idl', '.hlsl', '.pm', '.pl', '.cc', '.ush', '.usf',
                    '.mjs', '.inc', '.pyx', '.r', '.cuh', '.inl'],
            'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', 
                        '.dmg', '.pkg', '.deb', '.rpm', '.msi', '.cab', '.arj', '.lzh',
                        '.lha', '.ace', '.arc', '.wim', '.swm', '.esd', '.pak', '.tgz',
                        '.archive'],
            'Executables': ['.exe', '.dll', '.so', '.dylib', '.app', '.bin', '.msi', 
                           '.com', '.sys', '.drv', '.ocx', '.cpl', '.scr', '.pif', '.pyd',
                           '.class', '.jar', '.a', '.lib', '.o', '.dex', '.nca', '.suprx'],
            'System': ['.sys', '.ini', '.conf', '.config', '.reg', '.dat', '.log', '.tmp',
                      '.temp', '.cache', '.db', '.sqlite', '.bak', '.old', '.dmp', '.hiv',
                      '.evtx', '.etl', '.evt', '.blg', '.perf', '.etl', '.manifest', '.cat',
                      '.mui', '.mum', '.meta', '.mof', '.nls', '.mo', '.cdxml', '.adml',
                      '.admx', '.mun', '.debug', '.tlb', '.pnf', '.lock', '.msc', '.plist',
                      '.vdf'],
            'Fonts': ['.ttf', '.otf', '.woff', '.woff2', '.eot', '.sfnt', '.bdf', '.pcf',
                     '.pfa', '.pfb', '.ttc', '.dfont', '.pfm', '.afm', '.pf2', '.pfr'],
            '3D Models': ['.obj', '.fbx', '.3ds', '.max', '.blend', '.dae', '.stl', '.ply',
                         '.glb', '.gltf', '.usd', '.usda', '.usdc', '.usdz', '.abc', '.bvh',
                         '.x3d', '.x3db', '.x3dv', '.wrl', '.vrml', '.pskx', '.psk', '.xyz',
                         '.md5mesh', '.prefab', '.asset'],
            'Web': ['.html', '.htm', '.css', '.js', '.php', '.asp', '.aspx', '.jsp', 
                   '.json', '.xml', '.svg', '.webp', '.woff', '.woff2', '.eot', '.ttf',
                   '.otf', '.scss', '.sass', '.less', '.styl', '.coffee', '.ts', '.jsx',
                   '.qml', '.qmlc', '.qmltypes', '.xaml'],
            'Games': ['.rom', '.iso', '.bin', '.cue', '.gba', '.nds', '.3ds', '.cia', '.cci',
                     '.sav', '.srm', '.state', '.zst', '.z64', '.v64', '.n64', '.gb', '.gbc',
                     '.gba', '.nds', '.3ds', '.cia', '.cci', '.sav', '.srm', '.state',
                     '.uasset', '.uexp', '.ubulk', '.umap', '.rpgmvp', '.gnf', '.gxt',
                     '.shader', '.compute', '.shadergraph', '.shadersubgraph'],
            'Other': []
        }
        
        if not extension:
            return 'No Extension'
            
        for category, extensions in categories.items():
            if extension.lower() in extensions:
                return category
                
        return 'Other'

    def analyze_directory(self, directory):
        """Recursively analyze files in the given directory."""
        for root, _, files in os.walk(directory):
            for file in files:
                try:
                    file_path = os.path.join(root, file)
                    file_size = os.path.getsize(file_path)
                    file_extension = os.path.splitext(file)[1]
                    
                    self.file_sizes.append(file_size)
                    file_type = self.get_file_type_category(file_extension)
                    self.file_types[file_type] += 1
                    
                    if file_type == 'Other (Unknown Extension)':
                        self.other_types[file_extension.lower()] += 1
                except (PermissionError, FileNotFoundError):
                    continue

    def plot_histogram(self):
        """Plot histogram of file sizes."""
        plt.figure(figsize=(12, 6))

        valid_sizes = [size for size in self.file_sizes if size > 0]
        
        if not valid_sizes:
            print("Warning: No valid file sizes found for histogram")
            plt.close()
            return

        min_size = min(valid_sizes)
        max_size = max(valid_sizes)

        min_size = max(min_size, 1)
        

        bins = np.logspace(np.log10(min_size), np.log10(max_size), 50)
        
        plt.hist(valid_sizes, bins=bins, edgecolor='black')
        plt.title('Distribution of File Sizes')
        plt.xlabel('File Size (bytes)')
        plt.ylabel('Number of Files')
        plt.xscale('log')
        plt.grid(True)

        size_labels = ['1KB', '10KB', '100KB', '1MB', '10MB', '100MB', '1GB', '10GB']
        size_values = [1024, 10*1024, 100*1024, 1024*1024, 10*1024*1024, 
                      100*1024*1024, 1024*1024*1024, 10*1024*1024*1024]
        
        valid_labels = [(label, value) for label, value in zip(size_labels, size_values) 
                       if min_size <= value <= max_size]
        if valid_labels:
            labels, values = zip(*valid_labels)
            plt.xticks(values, labels, rotation=45)
        
        plt.tight_layout()
        plt.savefig('file_size_histogram.png')
        plt.close()

    def plot_pie_chart(self):
        """Plot pie chart of file types with non-overlapping labels."""
        plt.figure(figsize=(14, 14))

        labels = list(self.file_types.keys())
        sizes = list(self.file_types.values())

        threshold = 0.01 * sum(sizes)
        filtered_labels = [label if size > threshold else '' for label, size in zip(labels, sizes)]


        wedges, texts, autotexts = plt.pie(
            sizes,
            labels=filtered_labels,
            autopct=lambda p: f'{p:.1f}%' if p > 1 else '',
            startangle=140,
            pctdistance=0.85,
            textprops={'fontsize': 12},
            wedgeprops={'linewidth': 1, 'edgecolor': 'white'}
        )

        plt.legend(
            wedges,
            labels,
            title="File Types",
            loc="center left",
            bbox_to_anchor=(1, 0.5),
            fontsize=12
        )

        plt.title('Distribution of File Types', pad=20, fontsize=16)
        plt.tight_layout()
        plt.savefig('file_type_distribution.png', bbox_inches='tight')
        plt.close()

    def plot_cdf(self):
        """Plot cumulative distribution function of file sizes."""
        plt.figure(figsize=(12, 6))
        sorted_sizes = np.sort(self.file_sizes)
        p = np.arange(1, len(sorted_sizes) + 1) / len(sorted_sizes)
        plt.plot(sorted_sizes, p)
        plt.title('Cumulative Distribution Function of File Sizes')
        plt.xlabel('File Size (bytes)')
        plt.ylabel('Cumulative Probability')
        plt.xscale('log')
        plt.grid(True)
        plt.savefig('file_size_cdf.png')
        plt.close()

    def generate_report(self):
        """Generate a comprehensive report of the analysis."""
        total_files = len(self.file_sizes)
        total_size = sum(self.file_sizes)
        
        print("\nFile System Analysis Report")
        print("=" * 50)
        print(f"Total number of files: {total_files}")
        print(f"Total size: {total_size / (1024*1024):.2f} MB")
        print("\nFile Type Distribution:")
        for file_type, count in self.file_types.items():
            percentage = (count / total_files) * 100
            print(f"{file_type}: {count} files ({percentage:.1f}%)")
        
        if self.other_types:
            with open('other_category_analysis.txt', 'w', encoding='utf-8') as f:
                f.write("Files with Unknown Extensions:\n")
                f.write("-" * 30 + "\n")

                sorted_others = sorted(self.other_types.items(), key=lambda x: x[1], reverse=True)
                for ext, count in sorted_others:
                    percentage = (count / total_files) * 100
                    f.write(f"{ext}: {count} files ({percentage:.1f}%)\n")
            print("\nUnknown extensions analysis has been saved to 'other_category_analysis.txt'")
        

        self.plot_histogram()
        self.plot_pie_chart()
        self.plot_cdf()
        print("\nVisualizations have been saved as PNG files.")

def main():
    analyzer = FileSystemAnalyzer()
    

    directory = input("Enter the directory path to analyze: ")
    
    if not os.path.exists(directory):
        print("Error: Directory does not exist!")
        return
    
    print(f"Analyzing directory: {directory}")
    analyzer.analyze_directory(directory)
    analyzer.generate_report()

if __name__ == "__main__":
    main() 