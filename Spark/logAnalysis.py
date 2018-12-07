#########################
# Pre-processing steps:
# i) write a fnc to individually parse each row of record first
# ii) pass fnc in (i) to map() applied onto a line of text RDD
#########################

# step(i): identify validity of each log line, if correct, parse it into Row objects in RDD. 
def parseApacheLogLine(logline):
	match = re.search(APACHE_ACCESS_LOG_PATTERN, logline)	#ret: MatchObject instance; splittable by group()
	if match is None:
		return(logline, 0)
	else:
		return (Row(		#spark Row() object allows each record in RDD accessed by '.' 
		host = match.group(1),		#get one field in one record: access_logs.map(lambda x: x.host)	
		client_identd = match.group(2),
		...
		), 1)

# step(ii)
def parseLogs():
	parsed_logs = sc.textFile(logFile).map(parseApacheLogLine).cache()

		
		
# filter by Key
hostMoreThan10 = hostSum.filter(lambda s: s[1] > 10)

topEndpoints = endpointsCounts.takeOrdered(10, lambda s: -1*s[1])

# use a label to classify valid and invalid rows of records 
access_log = parsed_log.filter(lambda s: s[1]==1).map(lambda s:s[0]).cache()
# here, it returns RDDs of valid parsed logs; i.e. a collection of valid records

#optimize: skip groupByKey()
code = access_logs.map(lambda x: (x.response_code, 1)).groupByKey().reduceByKey(add).cache()		#groupByKey() in-RDD combiner: recall one partition, one machine, one RDD; thus, combine before shuffling
# just use reduceByKey() directly on map() outputs 
code = access_logs.map(lambda x: (x.response_code, 1)).reduceByKey(add).cache()

#plot a graph
labels = responseCodeToCount.map(lambda (x,y): x).collect()
print labels	#only after collect() can we call on labels 
count = access_logs.count()
fracs = responseCodeToCount.map(lambda (x,y): (float(y)/count)).collect()		#collect() return a list of elements 

########################
# 2 approaches taking top 10 frequent items
########################

#M1: takeOrdered()
mostVisitedHost = access_logs.map(lambda x: (x.host, 1)).reduceByKey(add).takeOrdered(10, lambda y: -y[1])		#takeOrdered() is an action

#M2: filter()
mostVisitedHost = access_logs.map(lambda x: (x.host, 1)).reduceByKey(add).filter(lambda q: q[1]>10)


#take top 5 by name, not by tuples
hostsPick20 = hostMoreThan10.map(lambda x: x[0]).take(20)


########################
# Graph plotting
########################
endpoints = (access_logs
             .map(lambda log: (log.endpoint, 1))
             .reduceByKey(add)
             .cache())
ends = endpoints.map(lambda (x, y): x).collect()		#collect() returns a list of x values 
counts = endpoints.map(lambda (x, y): y).collect()

fig = plt.figure(figsize=(8,4.2), facecolor='white', edgecolor='white')
plt.axis([0, len(ends), 0, max(counts)])
plt.grid(b=True, which='major', axis='y')
plt.xlabel('Endpoints')
plt.ylabel('Number of Hits')
plt.plot(counts)
display(fig)

numUniqueHosts = access_logs.map(lambda x: x.host).distinct().count()

#hourly unique host list : [(hour, #unique hosts)]
hourlyHostsList = access_logs.map(lambda x: (x.date_time.hour , x.host)).distinct().groupByKey().reduceByKey(len)		#mapValues() also okay: cz groupByKey ensure one key per list 

#Average Number of Hourly Requests per Host
hourly_request = access_logs.map(lambda x: (x.date_time.hour,1)).reduceByKey(add)
# [(hour,#requests)]

#after join: [(hour, (#requests, #unique_hosts))]
avgHourlyReqPerHost = hourly_request.join(hourlyHostsList).map(lambda (hour, (req, uniqueH)): )
# WRONG: mean is not communitative and not associative!!

#combine count with mean
hourAndHost = access_logs.map(lambda log:(log.date_time.hour, log.host)).groupByKey()
						 .sortByKey()
						 .map(lambda x: (x[0], len(x[1])/len(set(x[1])))).cache()

#trap of filter(): still returns Row()
# each record in a rdd is a spark Row() object
badRecoerds = access_logs.filter(lambda x: x.response_code==404).cache()

