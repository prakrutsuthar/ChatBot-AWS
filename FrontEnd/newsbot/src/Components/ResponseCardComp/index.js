import React from "react";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";

function ResponseCardComp(props) {
  return (
    <Card
    sx={{
      minWidth: 275,
      m: 0.5,
      backgroundColor: "#98CDBF",
      color: "black",
      borderRadius: 5,
    }}
  >
    <CardContent>
      <Typography sx={{ fontSize: 12, fontWeight: "bold" }} gutterBottom>
        NewsBot
      </Typography>
      <Typography sx={{ fontSize: 14 }} color="black" component="div">
        {props.text}
      </Typography>
    </CardContent>
  </Card>
  );
}

export default ResponseCardComp;
