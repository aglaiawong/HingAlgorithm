/*
Frequency at STRIPE
*/

private static class MyReducer extends
		Reducer<Text, HashMapStringIntWritable, PairOfStrings, FloatWritable> {

	// Reuse objects.
	private final static HashMapStringIntWritable SUM_STRIPES = new HashMapStringIntWritable();
	private final static PairOfStrings BIGRAM = new PairOfStrings();
	private final static FloatWritable FREQ = new FloatWritable();

	@Override
	public void reduce(Text key,
			Iterable<HashMapStringIntWritable> stripes, Context context)
			throws IOException, InterruptedException {

		/*	use of iterables: 
			i) use an iterator to loop thru iterables
			ii) check before you get: iter.hasNext() --> iter.next()
		*/	
			
		Iterator<HashMapStringIntWritable> iter = stripes.iterator();
		while (iter.hasNext()) {
			SUM_STRIPES.plus(iter.next());
		}

		/*	Iterate thru HashMap in java
			i) Map.Entry<T> e: target.entrySet()	//entrySet(): key=value
			ii) e.getKey() and e.getValue()
		*/
		
		float MARGINAL = 0;
		for (Map.Entry<String, Integer> e : SUM_STRIPES.entrySet()) {
			MARGINAL += e.getValue();
		}
		BIGRAM.set(key.toString(), "");
		FREQ.set(MARGINAL);
		context.write(BIGRAM, FREQ);		//emit(<"", MARGINAL>)

		for (Map.Entry<String, Integer> e : SUM_STRIPES.entrySet()) {
			BIGRAM.set(key.toString(), e.getKey());
			FREQ.set(SUM_STRIPES.get(e.getValue()) / MARGINAL);
			context.write(BIGRAM, FREQ);
		}
		SUM_STRIPES.clear();	//reuse objects need to be cleared out before next fnc call
	}
}

/*
	Partitioner: used for shuffling k/v pairs ; to hash against each records; 
*/
	private static class MyPartitioner extends
			Partitioner<PairOfStrings, IntWritable> {
		@Override
		public int getPartition(PairOfStrings key, IntWritable value,
				int numReduceTasks) {		//parameter list tells you it operates on k/v pair basis 
			return (key.getLeftElement().hashCode() & Integer.MAX_VALUE)
					% numReduceTasks;
		}
	}


	
/*
Some general operators 
*/	
context.write(k,v);
UDV.set()


