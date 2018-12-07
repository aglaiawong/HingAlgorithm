private static class MyMapper extends Mapper<LongWritable, Text, PairOfStrings, IntWritable>{
	
	// obj reuse to save overhead of object creation 
	// these objects are for MR, i.e. object meant to be transferred in network, thus requires serialization and deserialization
	
	private static final IntWritable ONE = new IntWritable(1);
	private static final PairOfStrings BIGRAM = new PairOfStrings();
	private static final PairOfStrings EMPTY_BIGRAM = new PairOfStrings();
	
	public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedByTimeoutException{
		//key: document name; value: document content
		// basic 3 elements of mapper/reducer/combiner: key, value(iterable or not), context
		
		String line = ((Text) value).toString();
		String[] words = line.trim().split("\\s+")
		
		for(int i=0; i<words.length-1; i++){
			EMPTY_BIGRAM.set(words[i], "");
			BIGRAM.set(words[i], words[i+1]);		//use set() for object 
			
			context.write(BIGRAM, ONE);
			context.write(EMPTY_BIGRAM, ONE);
			
		}
	}

}	
	
private static class MyPartitioner extends Partitioner<PairOfStrings, IntWritable>{
	@Override
	public int getPartition(PairOfStrings key, IntWritable value, int numReduceTasks){
		return (key.getLeftElement().hashCode() & Integer.MAX_VALUE)%numReduceTasks;
	}
}

//combiner same code as reducer 
	private static class MyCombiner extends
			Reducer<PairOfStrings, IntWritable, PairOfStrings, IntWritable> {
		
		// Reuse objects.
		private final static IntWritable SUM = new IntWritable();

		@Override
		public void reduce(PairOfStrings key, Iterable<IntWritable> values,
				Context context) throws IOException, InterruptedException {
			/*
			 * TODO: Your implementation goes here. The output must be a
			 * sequence of key-value pairs of <bigram, count>
			 */
			 int sum = 0;
			 for(IntWritable v:values){
				 sum+=v.get();
			 }
			 
			 SUM.set(sum);
			 context.write(key, SUM);
		}
}


// set the classes to job
job.setMapperClass(MyMapper.class);
job.setReducerClass(MyReducer.class);
job.setCombinerClass(MyCombiner.class);
job.setPartitionerClass(MyPartitioner.class);




package com.tutorialspoint;

import java.util.*;

public class HashMapDemo {
   public static void main(String args[]) {
      
      // create hash map
      HashMap newmap = new HashMap();

      // populate hash map
      newmap.put(1, "tutorials");
      newmap.put(2, "point");
      newmap.put(3, "is best"); 

      System.out.println("Initial map elements: " + newmap);

      // clear hash map
      newmap.clear();

      System.out.println("Map elements after clear: " + newmap);
   }    
}









