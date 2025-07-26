# Inventory Management System

A comprehensive inventory and sales management system implemented in two different technologies: **Shell Script** (CLI-based) and **Python with Tkinter** (GUI-based). Both versions provide complete functionality for managing inventory, processing sales, generating reports, and handling customer data.

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Shell Script Version](#shell-script-version)
- [Python GUI Version](#python-gui-version)
- [File Descriptions](#file-descriptions)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### Core Functionality
- **Inventory Management**: Add, update, delete, and search products
- **Sales Processing**: Record sales transactions and update inventory
- **Customer Management**: Maintain customer database and transaction history
- **Reporting System**: Generate comprehensive sales and inventory reports
- **Data Persistence**: All data stored in text files for reliability
- **Error Handling**: Robust error handling and input validation
- **Menu-driven Interface**: Intuitive navigation in both versions

### Advanced Features
- **Dual Implementation**: Choose between command-line (Shell) or graphical interface (Python/Tkinter)
- **Real-time Updates**: Inventory automatically updates after each sale
- **Search Functionality**: Quick product and customer search capabilities
- **Report Generation**: Detailed sales reports and inventory status
- **User-friendly Design**: Clean, organized interface in both versions

## 📁 Project Structure

```
inventory-management-system/
├── README.md
├── LICENSE
├── .gitignore
├── shell-version/
│   ├── Scripts/
│   │   ├── bill.txt
│   │   ├── customers.txt
│   │   ├── error.txt
│   │   ├── inventory.txt
│   │   ├── inventoryMenu.txt
│   │   ├── logs.txt
│   │   ├── LsReport.txt
│   │   ├── PMS.txt
│   │   ├── reportMenu.txt
│   │   ├── sales.txt
│   │   ├── salesOp.txt
│   │   ├── salesPerMedName.txt
│   │   └── searchMenu.txt
│   └── README.md
└── python-version/
    ├── bill.txt
    ├── customers.txt
    ├── error.txt
    ├── inventory.txt
    ├── inventoryMenu.txt
    ├── logs.txt
    ├── LsReport.txt
    ├── PMS.txt
    ├── reportMenu.txt
    ├── sales.txt
    ├── salesOp.txt
    ├── salesPerMedName.txt
    ├── searchMenu.txt
    └── README.md
```

## 🛠 Technologies Used

### Shell Script Version
- **Shell Scripting** (Bash)
- **Text file storage** for data persistence
- **CLI-based user interface**
- Compatible with Linux/Unix systems

### Python GUI Version
- **Python 3.x**
- **Tkinter** for GUI development
- **Text file storage** for data persistence
- Cross-platform compatibility (Windows, macOS, Linux)

## 🚀 Installation & Setup

### Prerequisites
- **For Shell Version**: Unix/Linux environment with Bash shell
- **For Python Version**: Python 3.6 or higher

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/inventory-management-system.git
   cd inventory-management-system
   ```

2. **For Shell Script Version**
   ```bash
   cd shell-version
   chmod +x Scripts/*.txt  # Make scripts executable if needed
   ```

3. **For Python Version**
   ```bash
   cd python-version
   # No additional dependencies required (uses built-in Tkinter)
   ```

## 📖 Usage

### Shell Script Version
```bash
cd shell-version/Scripts
./PMS.txt  # Main program launcher
```

### Python GUI Version
```bash
cd python-version
python PMS.py  # or python3 PMS.py
```

## 🖥 Shell Script Version

The Shell script version provides a command-line interface with the following features:

### Key Components
- **Main Menu**: Central navigation hub
- **Inventory Management**: Add/edit/delete products
- **Sales Processing**: Process customer transactions
- **Report Generation**: View sales and inventory reports
- **Search Functionality**: Find products and customers quickly

### Navigation
- Uses numbered menu options
- Input validation for all user entries
- Clear error messages and prompts
- Automatic return to main menu after operations

## 🖼 Python GUI Version

The Python version offers a modern graphical user interface built with Tkinter:

### Key Components
- **Main Window**: Central application interface
- **Dialog Boxes**: For data entry and confirmation
- **List Views**: Display inventory and sales data
- **Form Widgets**: User-friendly input forms
- **Menu Bar**: Quick access to all functions

### User Experience
- Point-and-click interface
- Real-time data updates
- Visual feedback for all operations
- Responsive design elements

## 📄 File Descriptions

| File | Purpose |
|------|---------|
| `PMS.txt` | Main program launcher and menu system |
| `inventory.txt` | Product inventory data storage |
| `sales.txt` | Sales transaction records |
| `customers.txt` | Customer information database |
| `bill.txt` | Bill generation templates |
| `reports.txt` | Report generation logic |
| `error.txt` | Error logging and handling |
| `logs.txt` | System activity logs |

## 📊 Data Structure

### Inventory Format
```
ProductID | ProductName | Quantity | Price | Category
```

### Sales Format
```
SaleID | Date | ProductID | Quantity | CustomerID | Total
```

### Customer Format
```
CustomerID | Name | Phone | Email | Address
```

## 🤝 Contributing

We welcome contributions to improve both versions of the inventory management system!

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow existing code style and conventions
- Test thoroughly before submitting
- Update documentation as needed
- Ensure compatibility with both versions

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built as a learning project to demonstrate different programming approaches
- Showcases the versatility of implementing the same functionality in different technologies
- Thanks to the open-source community for inspiration and resources

## 📞 Support

If you encounter any issues or have questions:
- Open an issue in the GitHub repository
- Check existing documentation
- Review the code comments for implementation details

---

**Note**: Both versions maintain the same data format and functionality, allowing you to switch between CLI and GUI interfaces while maintaining data consistency.
