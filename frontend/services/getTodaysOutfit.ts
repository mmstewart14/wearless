const getTodaysOutfit = async () => {
  return await fetch(
    "https://7crxjhgccawqjvwtwwetfa2a7i0hknna.lambda-url.us-east-2.on.aws/",
    {
      method: "GET",
      headers: {
        Accept: "application/json",
      },
    }
  )
    .then((response) => response.json())
    .catch((error) => {
      console.error(error);
    });
};

export default getTodaysOutfit;
