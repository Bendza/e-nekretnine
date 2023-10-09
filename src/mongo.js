const { MongoClient } = require("mongodb");

const url = "mongodb://127.0.0.1:27017";

async function connectToDatabase() {
  const client = await MongoClient.connect(url, { useUnifiedTopology: true });
  return client;
}

async function fetchData(filters = {}) {
  let client;

  try {
    client = await connectToDatabase();
    const db = client.db("e-nekretnine");
    const collection = db.collection("ads_spider");

    const query = {};

    if (filters.street) {
      query.street = { $regex: new RegExp(filters.street, "i") };
    }
    if (filters.city) {
      query.city = filters.city;
    }
    if (filters.priceFrom && filters.priceTo) {
        query.price = {
            $gte: filters.priceFrom,
            $lte: filters.priceTo
        };
    }
    if (filters.surfaceFrom && filters.surfaceTo) {
        query.surface = {
            $gte: filters.surfaceFrom,
            $lte: filters.surfaceTo
        };
    }
    if (filters.date) {
        query.date = {
            $gt: filters.date, 
        };
    }
    if (filters.objectType) {
      query.objectType = filters.objectType;
    }
    if (filters.adType) {
      query.adType = filters.adType;
    }

    const docs = await collection.find(query).limit(50).toArray();
    console.log('Query string:',query);
    return docs;
  } catch (err) {
    throw err;
  } finally {
    if (client) client.close();
  }
}

module.exports = {
  fetchData,
};
