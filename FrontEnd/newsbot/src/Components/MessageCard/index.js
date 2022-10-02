import React from "react";
import Card from "@mui/material/Card";
import CardActions from "@mui/material/CardActions";
import CardContent from "@mui/material/CardContent";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";

function MessageCardComp(props) {
  return (
    <Card
      sx={{
        minWidth: 275,
        m: 0.5,
        backgroundColor: "#eab676",
        color: "black",
        borderRadius: 5,
      }}
    >
      <CardContent>
        <Typography sx={{ fontSize: 12, fontWeight: "bold" }} gutterBottom>
          User
        </Typography>
        <Typography sx={{ fontSize: 14 }} color="black" component="div">
          {props.text}
        </Typography>
      </CardContent>
    </Card>
  );
}

export default MessageCardComp;
