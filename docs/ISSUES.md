# ISSUES

### Error en /src/database_config.py
###### *Al guardar los datos de port se guardan correctamente en /config/database.config pero al leerlos se eliminan dos dígitos.*

* ##### Posible error en el método `setupUi()`.
 ``` [python]
name = f.readLine(255);
username = f.readLine(255);
password = f.readLine(255); # ValueError: invalid literal for int() with base 10: ''
hostname = f.readLine(255);
port = f.readLine(21);
f.close();

self.dbName.setText(str(name)[17:-3]);
self.username.setText(str(username)[21:-3]);
self.password.setText(str(password)[21:-3]); # ValueError: invalid literal for int() with base 10: ''
self.hostname.setText(str(hostname)[21:-3]);
self.port.setValue(int(str(port)[17:-3]));
 ```

* ##### revisar también método `configure()`.
``` [python]
data = "database_name: " + self.dbName.text();
data += "\ndatabase_username: " + self.username.text();
data += "\ndatabase_password: " + self.password.text();
data += "\ndatabase_hostname: " + self.hostname.text();
data += "\ndatabase_port: " + self.port.text();

f = QFile("config/database.config");
f.remove("config/database.config");

if f.open(QIODevice.ReadWrite | QIODevice.Text):
    stream = QTextStream(f);
    stream << data;
    f.close();

self.close();
```
