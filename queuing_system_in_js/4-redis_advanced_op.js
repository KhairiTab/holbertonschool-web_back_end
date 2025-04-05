import redis from 'redis';
import { promisify } from 'util';

// Create a Redis client
const client = redis.createClient();

// Utility function to print Redis responses
const printRedisResponse = (err, response) => {
  if (err) {
    console.error('Redis Error:', err);
  } else {
    console.log('Reply:', response);
  }
};

// Data to store in the hash
const hashKey = 'HolbertonSchools';
const hashData = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2
};

// Store hash values using hset
for (const [field, value] of Object.entries(hashData)) {
  client.hset(hashKey, field, value, printRedisResponse);
}

// Display the hash using hgetall
client.hgetall(hashKey, (err, object) => {
  if (err) {
    console.error('Redis Error:', err);
  } else {
    console.log('Hash Stored in Redis:', object);
  }
  // Quit the Redis client after operations
  client.quit();
});
