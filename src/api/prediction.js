// import packages
import qs from "qs";
import axios from "axios";
import { closestMatch } from "closest-match";

const prediction = async (searchRequest, availableLocation, setHousePrice) => {
  // desctructure
  const { bath, bhk, name, sqft } = searchRequest;

  //   process POST request
  const { data } = await axios({
    method: "POST",
    url: "https://estima.onrender.com/getpredictedprice",
    data: qs.stringify({
      total_sqft: sqft,
      bath: bath,
      bhk: bhk,
      location: closestMatch(name, availableLocation) || name,
    }),
  });

  console.log(data);

  setHousePrice(data.estimated_price);
};

export default prediction;
