# Shell Script Inventory Management System

A command-line based inventory and sales management system built with Shell scripting. This version provides a text-based interface for managing products, processing sales, and generating reports.

## 🚀 Quick Start

### Prerequisites
- Unix/Linux environment with Bash shell
- Basic command line knowledge

### Running the Application
```bash
cd Scripts/
chmod +x *.txt  # Make scripts executable if needed
./PMS.txt       # Launch the main program
```

## 📋 Features

### Main Menu Options
1. **Inventory Management**
   - Add new products
   - Update existing inventory
   - Remove discontinued items
   - View current stock levels

2. **Sales Operations**
   - Process customer purchases
   - Generate bills automatically
   - Update inventory in real-time
   - Record transaction details

3. **Customer Management**
   - Add new customers
   - Update customer information
   - View purchase history
   - Search customer database

4. **Reporting System**
   - Daily/Monthly sales reports
   - Inventory status reports
   - Low stock alerts
   - Customer purchase summaries

5. **Search Functions**
   - Search products by name/ID
   - Find customers by various criteria
   - Filter sales by date range
   - Quick lookup features

## 🗂 File Structure

| File | Description |
|------|-------------|
| `PMS.txt` | Main program launcher and menu controller |
| `inventoryMenu.txt` | Inventory management interface |
| `salesOp.txt` | Sales operation handlers |
| `reportMenu.txt` | Report generation system |
| `searchMenu.txt` | Search functionality |
| `inventory.txt` | Product database |
| `sales.txt` | Sales transaction log |
| `customers.txt` | Customer information |
| `bill.txt` | Bill templates and generation |
| `logs.txt` | System activity logs |
| `error.txt` | Error handling and logging |

## 💻 Usage Examples

### Adding a New Product
```bash
# Navigate through: Main Menu > Inventory Management > Add Product
# Enter product details when prompted:
Product ID: P001
Product Name: Laptop Computer
Quantity: 50
Price: 999.99
Category: Electronics
```

### Processing a Sale
```bash
# Navigate through: Main Menu > Sales Operations > New Sale
# Enter sale details:
Customer ID: C001
Product ID: P001
Quantity: 2
# System automatically calculates total and updates inventory
```

### Generating Reports
```bash
# Navigate through: Main Menu > Reports > Sales Report
# Choose report type:
1. Daily Report
2. Monthly Report
3. Product-wise Sales
4. Customer-wise Sales
```

## 🔧 Customization

### Modifying Data Fields
Edit the respective `.txt` files to add custom fields:
- Product attributes in `inventory.txt`
- Customer fields in `customers.txt`
- Transaction details in `sales.txt`

### Adding New Features
1. Create new menu option in `PMS.txt`
2. Implement functionality in separate script
3. Update navigation logic
4. Test thoroughly

## 📊 Data Format

### Inventory Data Structure
```
ProductID|ProductName|Quantity|Price|Category|LastUpdated
P001|Laptop Computer|50|999.99|Electronics|2025-07-26
```

### Sales Data Structure
```
SaleID|Date|Time|ProductID|Quantity|CustomerID|UnitPrice|Total
S001|2025-07-26|14:30:00|P001|2|C001|999.99|1999.98
```

### Customer Data Structure
```
CustomerID|Name|Phone|Email|Address|RegistrationDate
C001|John Doe|+1234567890|john@email.com|123 Main St|2025-07-26
```

## 🛠 Troubleshooting

### Common Issues

**Script not executable**
```bash
chmod +x *.txt
```

**File not found errors**
- Ensure all `.txt` files are in the same directory
- Check file permissions
- Verify file names match exactly

**Data corruption**
- Keep backup copies of data files
- Check file format matches expected structure
- Validate data entries

### Debug Mode
Enable debug output by modifying script headers:
```bash
#!/bin/bash
set -x  # Enable debug mode
```

## 🔒 Security Notes

- Data is stored in plain text files
- No encryption implemented
- Suitable for local/trusted environments
- Consider adding authentication for production use

## 📝 Development Notes

### Code Style
- Use descriptive variable names
- Add comments for complex logic
- Follow consistent indentation
- Handle edge cases gracefully

### Testing
- Test all menu options
- Verify data persistence
- Check error handling
- Validate input sanitization

---

**Note**: This shell script version is designed for learning purposes and demonstrates core programming concepts in a Unix/Linux environment.