import axios from "axios";

const getLocation = async () => {
  const { data } = await axios({
    method: "GET",
    url: "https://estima.onrender.com/getlocation",
  });

  return data.location;
};

export default getLocation;
