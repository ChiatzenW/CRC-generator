 # Generate CRC model image from toml source.

## Usage:

Modify the crc_classes.toml to change the source. 

Add a new section for a new class. Then follow the format "responsibility"="collaborator \n another collaborator"

Run the python file to generate jpgs. They should be stored in a folder named "crc".

## Example

```toml
[class1]
"responsibility" = "collaborator"
"store some data" = "le_database \n asdsad \n sadsad"
"veeeeeeeeeeeeeeeeeeeeeeeerrrrrrrrrrrrrrrrrrrryloooooooooooooong"="dsa \n sad"
```

<img src="crc\class1.jpg"  />

```toml
[class2]
"tell a joke"="some joke class"
"r"="c"
```

<img src="crc/class2.jpg" />

