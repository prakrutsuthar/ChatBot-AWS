import React from "react";
import { Typography, Box, Grid, Link } from "@mui/material";

function DialogComp(props) {
  // props.renderr(Math.random());

  var refinedDate = props.date;
  refinedDate = refinedDate.substring(0, 10);

  return (
    <Grid
      sx={{
        border: 1,
        p: 1,
        borderRadius: 1,
        backgroundColor: "#DBDE96",
        color: "black",
        flexGrow:1
      }}
    >
      <Box
        component="div"
        sx={{
          pt: 1,
          pl: 3,
          fontSize: 16,
          fontFamily: "Arial",
          fontWeight: "bold",
        }}
      >
        ({props.ind}) Title: {props.title}
      </Box>
      {props.description != "" && (
        <Box
          component="div"
          sx={{
            pt: 1,
            pl: 3,
            fontSize: 16,
            fontFamily: "Arial",
            fontWeight: "bold",
          }}
        >
          Description: {props.description}
        </Box>
      )}

      <Box sx={{ pt: 1 }}></Box>

      <Link
        href={props.link}
        sx={{
          pt: 1,
          color: "blue",
          pl: 3,
          fontSize: 16,
          fontFamily: "Arial",
          fontWeight: "bold",
        }}
      >
        Link to the Article
      </Link>
      <Grid container>
        <Box sx={{ flexGrow: 1 }}></Box>
        <Box
          component="span"
          sx={{
            pr: 3,
            pb: 1,
            fontSize: 16,
            fontFamily: "Arial",
            fontWeight: "bold",
          }}
        >
          Date: {refinedDate}
        </Box>
      </Grid>
    </Grid>
  );
}

export default DialogComp;
