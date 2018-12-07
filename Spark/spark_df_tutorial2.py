#spark df
young = user.filter(users["age"] < 30)
# panda-like
young = user[user.age < 21]

young.select(young["name"], young["age"]+1)
young.groupBy("gender").count()

young.join(log, log["id"]==users["id"], "left_outer")
young.join(log, log.id==users.id, "left_outer")


df.registerTempTable("people")
sqlContext.sql("Select name, avg(age) from people group by name").show()

#infer schema
df = sqlContext.read.json("x.json")
df.printSchema()


#infer schema
from pyspark.sql import Row
rdd = sc.textFile("people.csv")
Person = Row("first_name", "last_name", "gender", "age")
# accessed by: p.first_name, p.last_name or p["first_name"]

def line_to_person(line):
	cells = line.split(",")
	cells[3] = int(cells[3])
	return Person(*cells)

peopleRDD = rdd.map(line_to_person)
df = peopleRDD.toDF()
df.select(df['first_name'], df['last_name'], (df['age']>45).as('middle_aged')).show(6)
df.select(df.first_name, df.last_name, (df.age>45).as('middle_aged')).show(6)

#another way
from collections import namedtuple
Person = namedtuple('Person', ['first_name', 'last_name', 'gender', 'age'])
rdd = sc.textFile("people.csv")
def line_to_person(line):
	cells = line.split(",")
	return Person(cells[0], cells[1],cells[2],cells[3])
peopleRDD = rdd.map(line_to_person)
df = peopleRDD.toDF()	

#UDF: perform lambda on each record
from pyspark.sql.functions import udf
younger = udf(lambda x: x-1)
df.select(df.first_name, df.last_name, younger(df.age)).show()
