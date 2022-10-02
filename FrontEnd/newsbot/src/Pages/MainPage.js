import NavbarComp from "../Components/Navbar";
import { Grid, Box } from "@mui/material";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import { TextField } from "@mui/material";
import { Paper } from "@mui/material";
import { Button, Typography } from "@mui/material";
import { useEffect, useState } from "react";
import { myResults } from "../Components/Main Header";
import MessageCardComp from "../Components/MessageCard";
import axios from "axios";
import { myResponse } from "../Components/Main Header/index1";
import ResponseCardComp from "../Components/ResponseCardComp";
import GenreComp from "../Components/GenreComp";
import DialogComp from "../Components/DialogComp";
import Avatar from "@mui/material/Avatar";
import Stack from "@mui/material/Stack";
import React from "react";

const darkTheme = createTheme({
  palette: {
    mode: "dark",
  },
});

const sessionID = "1234";

function MainPage() {
  const [searchKeyword, setSearchKeyword] = useState("");
  const [result, setResult] = useState({});
  const [tags, setTags] = useState([]);
  var hiddenMessage = false;
  var dataToDisplay = null;
  var [dataToDisplayData, setDataToDisplayData] = useState(null);

  var mytags = [];

  useEffect(() => {}, [dataToDisplayData]);

  const handleClick = async (e) => {
    const tempResult = {
      message: searchKeyword,
    };
    myResults.push(tempResult);

    var data = JSON.stringify({
      text: searchKeyword,
      session_id: sessionID,
    });

    var config = {
      method: "post",
      url: "http://3.237.13.47/get_response_1",
      headers: {
        "Content-Type": "application/json",
      },
      data: data,
    };

    await axios(config)
      .then(function(response) {
        // console.log(JSON.stringify(response));
        const AIresponse = {
          message: response.data.message,
        };
        myResponse.push(AIresponse);
        mytags = response.data.tags;
        hiddenMessage = response.data.hidden_message;
        dataToDisplay = response.data.data_to_display;
      })
      .catch(function(error) {
        console.log(error);
        console.log(error.message);
        console.log(error.response);
        console.log(error.request);
      });
    if (hiddenMessage === true) {
      setTags(mytags);
    }
    if (hiddenMessage === null && dataToDisplay !== null) {
      console.log(dataToDisplay);
      setTags([]);
    }
    if (hiddenMessage === null) {
      setTags([]);
    }
    setResult(tempResult);
    setDataToDisplayData(dataToDisplay);
  };

  const clickedTag = async (e) => {
    var data = JSON.stringify({
      text: e.target.id,
      session_id: sessionID,
    });

    var config = {
      method: "post",
      url: "http://3.237.13.47/get_response_2",
      headers: {
        "Content-Type": "application/json",
      },
      data: data,
    };

    console.log("data", data);

    await axios(config)
      .then(function(response) {
        // console.log(JSON.stringify(response));
        dataToDisplay = response.data.data_to_display;
      })
      .catch(function(error) {
        console.log(error);
      });
    // console.log("data", dataToDisplay);
    setDataToDisplayData(dataToDisplay);
    // setTags(mytags);
    console.log("tags", tags);
  };

  return (
    <ThemeProvider theme={darkTheme}>
      <Grid container spacing={0.5} justifyContent="center">
        <Grid item xs={12}>
          <NavbarComp />
        </Grid>

        <Grid item xs={12}>
          <Grid container sx={{ pt: 3, pb: 3 }} alignItems="center">
            <Box sx={{ mr: 1, pl: 15 }}>
              <Button color="secondary"
                onClick={() => window.location.reload(false)}
                variant="contained"
              >
                <Typography p={1}>Reset</Typography>
              </Button>
            </Box>
            <Box sx={{ flexGrow: 1, mr: 1, pl: 35 }}>
              <Paper>
                <TextField
                  id="searchKeyword"
                  name="searchKeyword"
                  type="search"
                  label="Please Enter a Query"
                  variant="filled"
                  onChange={(v) => setSearchKeyword(v.target.value)}
                  fullWidth
                />
              </Paper>
            </Box>
            <Box sx={{ flexGrow: 1, mr: 1, pr: 15 }}>
              <Button onClick={handleClick} variant="contained">
                <Typography p={1}>Search</Typography>
              </Button>
            </Box>
            <Typography p={1}>Sources:</Typography>
            <Stack direction="row" spacing={2} sx={{ ml: 1, pr:15 }}>
              <Avatar
                alt="Remy Sharp"
                src="https://reisa.ca/wp-content/uploads/2020/04/canada-gov-2.jpg"
              />
              <Avatar
                alt="Travis Howard"
                src="https://i.cbc.ca/1.4066392.1541713557!/fileImage/httpImage/cbc-logo-horizontal.jpg"
              />
              <Avatar
                alt="Cindy Baker"
                src="https://static.toiimg.com/photo/47529300.cms"
              />
            </Stack>
          </Grid>
        </Grid>

        <Grid item xs={12}>
          <Grid
            container
            justifyContent="center"
            alignItems="center"
            spacing={{ xs: 2, md: 3 }}
            columns={{ xs: 4, sm: 8, md: 12 }}
            sx={{ pt: 4, pb: 2 }}
          >
            {tags.length !== 0 && (
              <Typography sx={{ pr: 1 }}>Select a Genre: </Typography>
            )}
            {tags?.map((myVar) => {
              return (
                <Box sx={{ pt: 0.2, pr: 0.2 }}>
                  <Button id={myVar} onClick={clickedTag} variant="contained">
                    {myVar}
                  </Button>
                </Box>
              );
            })}
          </Grid>
        </Grid>

        <Grid item xs={3}>
          <Grid container direction="column" sx={{ pt: 3 }} alignItems="center">
            {myResults?.map((myVariable) => {
              return (
                <MessageCardComp
                  text={myVariable.message}
                  name={myVariable.name}
                />
              );
            })}
          </Grid>
        </Grid>
        <Grid item xs={3}>
          <Grid container direction="column" sx={{ pt: 3 }} alignItems="center">
            {myResponse?.map((myVariable) => {
              return (
                <ResponseCardComp
                  text={myVariable.message}
                  name={myVariable.name}
                />
              );
            })}
          </Grid>
        </Grid>

        <Grid
          container
          xs={6}
          sx={{ borderLeft: 1, pl: 10, pr: 10 }}
          alignItems="center"
        >
          {dataToDisplayData?.map((myVariable, index) => {
            return (
              <DialogComp
                title={myVariable.title}
                description={myVariable.description}
                date={myVariable.readable_time}
                link={myVariable.link}
                ind={index + 1}
              />
            );
          })}
        </Grid>

        <Grid item xs={6}>
          {/* Render somethign here */}
        </Grid>

        <Grid item xs={6}>
          {/* Render somethign here */}
        </Grid>
      </Grid>
    </ThemeProvider>
  );
}

export default MainPage;
