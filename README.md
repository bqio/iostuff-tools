### IOStuff

Python I/O library.

### Examples

#### Text Reader

```python
with TextReader("data.txt") as reader:
    contents = reader.read()
```

#### Text Writer

```python
with TextWriter("data.txt") as writer:
    writer.write("Hello")
```

#### Json Reader with Any

```python
with JsonReader("user.json") as user:
    print(user)
```

#### Json Reader with Generic

```python
class User:
    name: str

with JsonReader[User]("user.json") as user:
    print(user.name)
```

#### Json Writer with Any

```python
with JsonWriter("user.json") as writer:
    writer.write({"name": "bqio"})
```

#### Json Writer with Generic

```python
class User:
    name: str

with JsonWriter[User]("user.json") as writer:
    user = User()
    user.name = "bqio"
    writer.write(user)
```

#### CSV Reader

```python
with CSVReader("data.csv") as reader:
    for row in reader:
        print(row)
```

#### CSV Writer

```python
with CSVWriter("data.csv") as writer:
    writer.write_row([1, 2, 3])
    writer.write_rows([["bqio", 1, 2], ["bqio", 2, 1]])
```

#### Binary Reader

```python
with BinaryReader("data.bin") as reader:
    print(reader.read_byte())
    print(reader.read_uint())
    print(reader.read_utf8_string(4))
    print(reader.seek(14))
    print(reader.read_utf8_nt_string())
```

#### Binary Writer

```python
from iostuff.writers.binary import BinaryWriter, BinaryEndian


with BinaryWriter("data.bin", BinaryEndian.Big) as writer:
    writer.write_byte(2)
    writer.write_utf8_string("Hello")
```
