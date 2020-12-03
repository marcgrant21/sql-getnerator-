fh=open('project_3.sql','w')
#fh=fh.rstrip("\n")


from faker import Faker 

rec=500000
fake_data=Faker()



fh.write("create database project_3;"+"\n")
fh.write("use project_3;"+"\n\n")
fh.write("CREATE table Customer("+"\n\t""Customer_id int auto_increment not null,"+"\n\t""Customer_fname varchar(15) not null,"+"\n\t""Customer_lname varchar(15) not null,"+"\n\t""Customer_telephone varchar(11) not null,"+"\n\t""Customer_email varchar(50) not null,"+"\n\t""Password varchar(300)not null,"+"\n\t""PRIMARY KEY(Customer_id))"+"\n"+"ENGINE=InnoDB;"+"\n\n");

fh.write("create table CreditCardDetails("+"\n\t""card_num varchar(15) not null,"+"\n\t""expiration_month varchar(2) not null,"+"\n\t""expiration_year varchar(4) not null,"+"\n\t""PRIMARY KEY(card_num))"+"\n"+"ENGINE=InnoDB;"+"\n\n");

fh.write("create table CustomerCreditCard("+"\n\t"" Customer_id int not null,"+"\n\t""card_num varchar(15) not null,"+"\n\t""foreign key(Customer_id) references Customer(Customer_id) on DELETE cascade on UPDATE cascade,"+"\n\t""foreign key(card_num) references CreditCardDetails(card_num) on DELETE cascade on UPDATE cascade,"+"\n\t""PRIMARY KEY(Customer_id,card_num))"+"\n"+"ENGINE=InnoDB;"+"\n\n");


fh.write("create table Branch("+"\n\t""br_id varchar(50) not null,"+"\n\t""name varchar(100) not null,"+"\n\t""street varchar(100) not null,"+"\n\t""city varchar(100) not null,"+"\n\t""telephone varchar(10) not null,"+"\n\t""PRIMARY KEY(br_id))"+"\n"+"ENGINE=InnoDB;"+"\n\n");


fh.write("CREATE table Supplier("+"\n\t""Supplier_id varchar(4) not null,"+"\n\t""Supplier_name varchar(15) not null,"+"\n\t""wh_id varchar(3) not null,"+"\n\t""Street_no varchar(30) not null,"+"\n\t""city varchar(20) not null,"+"\n\t""PRIMARY KEY(Supplier_id))"+"\n"+"ENGINE=InnoDB;"+"\n\n");





fh.write("Create table Product("+"\n\t""Product_id varchar(4) not null,"+"\n\t"" Product_descri varchar(250)not null,"+"\n\t""Model varchar(50) not null,"+"\n\t""Product_price double(20,2) not null,"+"\n\t""Prod_brand varchar(10) not null,"+"\n\t PRIMARY KEY(Product_id))"+"\n"+"ENGINE=InnoDB;"+"\n\n");

fh.write("create table Warehouse("+"\n\t""wh_id varchar(3) not null,"+"\n\t""street varchar(100) not null,"+"\n\t""city varchar(100) not null,"+"\n\t""telephone varchar(10) not null,"+"\n\t""PRIMARY KEY(wh_id))"+"\n"+"ENGINE=InnoDB;"+"\n\n");



fh.write("Create table Store("+"\n\t""wh_id varchar(3) not null,"+"\n\t""Product_id varchar(100) not null,"+"\n\t"" quantity int not null,"+"\n\t""PRIMARY KEY(wh_id,Product_id),"+"\n\t""foreign key(wh_id) references Warehouse(wh_id) on DELETE cascade on UPDATE cascade,"+"\n\t""foreign key(Product_id) references Product(Product_id) on DELETE cascade on UPDATE cascade)"+"\n"+"ENGINE=InnoDB;"+"\n\n");



fh.write("create table Carttotal("+"\n\t""Customer_id int not null,"+"\n\t""count_qty int not null,"+"\n\t""total double(20,2) not null,"+"\n\t""foreign key(Customer_id) references Customer(Customer_id) on DELETE cascade on UPDATE cascade,"+"\n\t""PRIMARY KEY(Customer_id))"+"\n"+"ENGINE=InnoDB;"+"\n\n");

fh.write("create table Receipt("+"\n\t""track_num varchar(7) not null,"+"\n\t""PRIMARY KEY(track_num))"+"\n"+"ENGINE=InnoDB;"+"\n\n");

fh.write("create table Checkout("+"\n\t""Customer_id int not null,"+"\n\t""track_num varchar(7) not null,"+"\n\t""total_cost double(20,2) not null,"+"\n\t""transaction_date date not null,"+"\n\t""primary key(Customer_id, track_num),"+"\n\t""foreign key(Customer_id) references Carttotal(Customer_id) on DELETE cascade on UPDATE cascade,"+"\n\t""foreign key(track_num) references Receipt(track_num) on DELETE cascade on UPDATE cascade)"+"\n"+"ENGINE=InnoDB;"+"\n\n");



fh.write("create table CartItems("+"\n\t""Customer_id int not null,"+"\n\t""Product_id varchar(4) not null,"+"\n\t""br_id varchar(50) not null,"+"\n\t""quantity int not null,"+"\n\t""cost double(10, 2) not null,"+"\n\t""date_added date not null,"+"\n\t""foreign key(Customer_id) references Carttotal(Customer_id) on DELETE cascade on UPDATE cascade,"+"\n\t""foreign key(Product_id) references Product(Product_id) on DELETE cascade on UPDATE cascade,"+"\n\t""PRIMARY KEY(Customer_id,Product_id))"+"\n"+"ENGINE=InnoDB;"+"\n\n");



fh.write("create table PurchasedItems("+"\n\t""pur_id int not null,"+"\n\t""Customer_id int not null,"+"\n\t""Product_id varchar(4) not null,"+"\n\t""br_id varchar(50) not null,"+"\n\t""cost double(20,2) not null,"+"\n\t""date_purchased date not null,"+"\n\t""foreign key(Customer_id) references Carttotal(Customer_id) on DELETE cascade on UPDATE cascade,"+"\n\t""foreign key(br_id) references Branch(br_id) on DELETE cascade on UPDATE cascade,"+"\n\t""PRIMARY KEY(pur_id))"+"\n"+"ENGINE=InnoDB;"+"\n\n");




fh.write("create table WriteReview("+"\n\t""Customer_id int not null,"+"\n\t""Product_id varchar(100) not null,"+"\n\t""rev_text text not null,"+"\n\t""date_written date not null,"+"\n\t""foreign key(Customer_id) references Customer(Customer_id) on DELETE cascade on UPDATE cascade,"+"\n\t""foreign key(Product_id) references Product(Product_id) on DELETE cascade on UPDATE cascade,"+"\n\t""PRIMARY KEY(Customer_id,Product_id))"+"\n"+"ENGINE=InnoDB;"+"\n\n");



fh.write("create table CustomerCarttotal("+"\n\t""Product_id varchar(100) not null,"+"\n\t""Customer_id int not null,"+"\n\t""br_id varchar(50) not null,"+"\n\t""foreign key(Customer_id) references Customer(Customer_id) on DELETE cascade on UPDATE cascade,"+"\n\t""foreign key(Product_id) references Product(Product_id) on DELETE cascade on UPDATE cascade,"+"\n\t""PRIMARY KEY(Customer_id,Product_id))"+"\n"+"ENGINE=InnoDB;"+"\n\n");





ed=1

for h in range(rec):
    ed=ed+1
    fh.write("INSERT INTO Customer VALUES")
    fh.write("('")
    fh.write(str(ed))
    fh.write(str("', '"+fake_data.first_name()+"',"+" '" ))
    fh.write(str(fake_data.last_name()+"',"+" '" ))
    fh.write(str(fake_data.random_int(min=8765432, max=9999999)))
    fh.write(str("',"+"'"+fake_data.email()))
    fh.write(str("',"+"'"+fake_data.password()+"');\n"))

jam=["Product Dimensions: 5.4 x 0.3 x 2.8 inches, Item Weight: 4.6 ounces , Battery type: Lithium ion","Product Dimensions: 7.3 x 4.2 x 4.3 inches, Item Weight: 8.6 ounces, Battery type: Lithium ion"]

bra=["HP","ACER","DELL","TOSHIBA","MACINTOSH","LENOVA","MSI"]


s=1
tan=100000
for u in range(tan):
	s=s+1
	fh.write("\n\n""INSERT INTO Product VALUES")
	fh.write("('")
	fh.write(str(s))
	fh.write("','")
	fh.write(str(fake_data.random.choice(jam)))
	fh.write("','")
	fh.write(str(fake_data.random_int(min=100, max=999)))
	fh.write("', '")
	fh.write(str(fake_data.random_int(min=10000, max=900000)))
	fh.write("','")
	fh.write(str(fake_data.random.choice(bra)+"');"))



mont=["01","02","03","04","05","06","07","08","09","10","11","12"]
zin=["2021","2022","2023"]

kk=3
for q in range(kk):
	fh.write("\n\n""INSERT INTO CreditCardDetails VALUES")
	fh.write("('")
	fh.write(str(fake_data.random_int(min=100000000000,max=999999999999))) 
	fh.write("','")
	fh.write(str(fake_data.random.choice(mont)))
	fh.write("','")
	fh.write(str(fake_data.random.choice(zin)+"');"))



xax=["Branch_1", "Branch_2 ", "Branch_3"]
treet=["Old Forge","Mountain View","Mona"]

ww=3

for x in range(ww):
	fh.write("\n\n""INSERT INTO Branch VALUES")
	fh.write("('")
	fh.write(str(fake_data.random_int(min=100, max=999)))
	fh.write("','")
	fh.write(str(fake_data.random.choice(xax)))
	fh.write("','")
	fh.write(str(fake_data.random.choice(treet)))
	fh.write("','")
	fh.write(str(fake_data.city()))
	fh.write("','")
	fh.write(str(fake_data.random_int(min=8765432, max=9999999)))
	fh.write("');")




wan=["13 Central"]


for h in range(1):
	fh.write("\n\n""INSERT INTO Warehouse VALUES")
	fh.write("('")
	fh.write(str(777))
	fh.write("','")
	fh.write(str(fake_data.random.choice(wan)))
	fh.write("','")
	fh.write(str(fake_data.city()))
	fh.write("','")
	fh.write(str(fake_data.random_int(min=8765432, max=9999999)))
	fh.write("');")
	


q=1
ee=11
for j in range(ee):
	q=q+1
	fh.write("\n\n""INSERT INTO Store VALUES")
	fh.write("('")
	fh.write(str(777))
	fh.write("','")
	fh.write(str(q))
	fh.write("','")
	fh.write(str(fake_data.random_int(min=1, max=1000)))
	fh.write("');")



fh.write("\n\n\n""DELIMITER //"+"\n""CREATE PROCEDURE getcost(IN Customer_id int,IN Product_id int,IN br_id int,IN quantity int,IN cost double(20,2))"+"\n\t""BEGIN"+"\n\t""INSERT INTO"+"\n""CartItems VALUES (Customer_id, Product_id, br_id, quantity ,quantity*cost, CURDATE());"+"\n\t""END //""\n""DELIMITER ;");




fh.write("\n\n\n""DELIMITER //"+"\n""CREATE PROCEDURE createACC(IN fname varchar(15),IN lname varchar(15),IN telephone varchar(11),IN email varchar(50),IN password varchar(300))"+"\n\t""BEGIN"+"\n\t""INSERT INTO"+"\n\t"" Customer(fname,lname,telephone,email,password,created_on) VALUES (fname ,lname ,telephone,email ,password ,CURDATE());"+"\n\t""END //""\n""DELIMITER ;");


fh.write("\n\n\n""DELIMITER //"+"\n\t""CREATE PROCEDURE addPurchasedItem(IN Customer_id int, IN Product_id int, IN br_id  int, IN cost double(20,2))"+"\n\t""BEGIN"+"\n\t""INSERT INTO"+"\n\t""PurchasedItems VALUES (Customer_id, Product_id, br_id, old.cost, CURDATE());"+"\n\t""END //""\n""DELIMITER ;");

fh.write("/* Triggers */");

fh.write("\n\n\n""DELIMITER $$"+"\n\t""CREATE TRIGGER newItem"+"\n\t""AFTER INSERT ON CartItems"+"\n\t""FOR EACH ROW"+"\n\t""BEGIN"+"\n\t""UPDATE Carttotal SET count_qty = count_qty + new.quantity, total = total + new.cost WHERE Customer_id = new.Customer_id;"+"\n\t""END $$"+"\n""DELIMITER ;");

fh.write("\n\n\n""DELIMITER $$"+"\n\t""CREATE TRIGGER updateItem"+"\n\t""AFTER UPDATE ON CartItems"+"\n\t""FOR EACH ROW"+"\n\t""BEGIN"+"\n\t""UPDATE  Carttotal SET count_qty = ((count_qty - old.quantity) + new.quantity), total = ((total - old.cost) + new.cost) WHERE Customer_id = new.Customer_id;"+"\n\t""END $$"+"\n""DELIMITER ;");


fh.write("\n\n\n""DELIMITER $$"+"\n\t""CREATE TRIGGER deleteItem"+"\n\t""AFTER DELETE ON CartItems"+"\n\t""FOR EACH ROW"+"\n\t""BEGIN"+"\n\t""UPDATE Carttotal SET count_qty = (count_qty - old.quantity), total = (total - old.cost) WHERE Customer_id = old.Customer_id;"+"\n\t""END $$"+"\n""DELIMITER ;");



fh.write("\n\n\ncreate database Branch_1;\n");
fh.write("use Branch_1;\n");

fh.write("Create table Product("+"\n\t""Product_id varchar(4) not null,"+"\n\t"" Product_descri varchar(250)not null,"+"\n\t""Model varchar(50) not null,"+"\n\t""Product_price double(20,2) not null,"+"\n\t""Prod_brand varchar(10) not null,"+"\n\t PRIMARY KEY(Product_id))"+"\n"+"ENGINE=InnoDB;"+"\n\n");


fh.write("Create table AmountInStock("+"\n\t""Product_id varchar(100)not null,"+"\n\t""quantity int not null,"+"\n\t""primary key(Product_id),"+"\n\t""foreign key(Product_id) references Product(Product_id) on DELETE cascade on UPDATE cascade)"+"\n"+"ENGINE=InnoDB;"+"\n\n");







lm=100
r=1

for u in range(lm):
	r=r+1
	fh.write("\n\n""INSERT INTO AmountInStock VALUES")
	fh.write("('")
	fh.write(str(r))
	fh.write(str("','"))
	fh.write(str(fake_data.random_int(min=20, max=500)))
	fh.write(str("');"))




fh.write("\n\n\n""DELIMITER //"+"\n""CREATE PROCEDURE purchaseItem(IN mode_id varchar(15),Amount int)"+"\n\t""BEGIN"+"\n\t""UPDATE AmountInStock SET quantity=(quantity - Amount) WHERE Product_id = mode_id;"+"\n\t""END //""\n""DELIMITER ;");




fh.write("\n\n\ncreate database Branch_2;\n");
fh.write("use Branch_2;\n");


fh.write("Create table Product("+"\n\t""Product_id varchar(4) not null,"+"\n\t"" Product_descri varchar(250)not null,"+"\n\t""Model varchar(50) not null,"+"\n\t""Product_price double(20,2) not null,"+"\n\t""Prod_brand varchar(10) not null,"+"\n\t PRIMARY KEY(Product_id))"+"\n"+"ENGINE=InnoDB;"+"\n\n");


fh.write("Create table AmountInStock("+"\n\t""Product_id varchar(100)not null,"+"\n\t""quantity int not null,"+"\n\t""primary key(Product_id),"+"\n\t""foreign key(Product_id) references Product(Product_id) on DELETE cascade on UPDATE cascade)"+"\n"+"ENGINE=InnoDB;"+"\n\n");




lm=100
r=1

for u in range(lm):
	r=r+1
	fh.write("\n\n""INSERT INTO AmountInStock VALUES")
	fh.write("('")
	fh.write(str(r))
	fh.write(str("','"))
	fh.write(str(fake_data.random_int(min=20, max=500)))
	fh.write(str("');"))




fh.write("\n\n\n""DELIMITER //"+"\n""CREATE PROCEDURE purchaseItem(IN mode_id varchar(15),Amount int)"+"\n\t""BEGIN"+"\n\t""UPDATE AmountInStock SET quantity=(quantity - Amount) WHERE Product_id = mode_id;"+"\n\t""END //""\n""DELIMITER ;");




fh.write("\n\n\ncreate database Branch_3;\n");
fh.write("use Branch_3;\n");


fh.write("Create table Product("+"\n\t""Product_id varchar(4) not null,"+"\n\t"" Product_descri varchar(250)not null,"+"\n\t""Model varchar(50) not null,"+"\n\t""Product_price double(20,2) not null,"+"\n\t""Prod_brand varchar(10) not null,"+"\n\t PRIMARY KEY(Product_id))"+"\n"+"ENGINE=InnoDB;"+"\n\n");


fh.write("Create table AmountInStock("+"\n\t""Product_id varchar(100)not null,"+"\n\t""quantity int not null,"+"\n\t""primary key(Product_id),"+"\n\t""foreign key(Product_id) references Product(Product_id) on DELETE cascade on UPDATE cascade)"+"\n"+"ENGINE=InnoDB;"+"\n\n");





lm=100
r=1

for u in range(lm):
	r=r+1
	fh.write("\n\n""INSERT INTO AmountInStock VALUES")
	fh.write("('")
	fh.write(str(r))
	fh.write(str("','"))
	fh.write(str(fake_data.random_int(min=20, max=500)))
	fh.write(str("');"))




fh.write("\n\n\n""DELIMITER //"+"\n""CREATE PROCEDURE purchaseItem(IN mode_id varchar(15),Amount int)"+"\n\t""BEGIN"+"\n\t""UPDATE AmountInStock SET quantity=(quantity - Amount) WHERE Product_id = mode_id;"+"\n\t""END //""\n""DELIMITER ;");






	

































fh.close()
	
	























