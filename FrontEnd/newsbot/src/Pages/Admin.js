import React from "react";
import { Grid, Box } from "@mui/material";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import NavbarComp from "../Components/Navbar";
import { Typography, Button } from "@mui/material";

function Admin() {
  const darkTheme = createTheme({
    palette: {
      mode: "dark",
    },
  });

  return (
    <ThemeProvider theme={darkTheme}>
      <Grid container spacing={0.5} justifyContent="center">
        <Grid item xs={12}>
          <NavbarComp />
        </Grid>
      </Grid>

      <Grid item xs={12}>
        <Grid container direction="column" alignItems="center">
          <Typography
            sx={{
              mt: 5,
              fontFamily: "monospace",
              fontWeight: 900,
              letterSpacing: ".3rem",
              color: "black",
              textDecoration: "none",
              fontSize: 45,
              textAlign: "center",
              pb:5
            }}
          >
            Admin
          </Typography>
          <Grid container direction="column" alignItems="center" sx={{ border: 1, maxWidth:500 }}>
            <Box sx={{ pt: 3 }}>
              <Typography
                sx={{
                  fontFamily: "monospace",
                  fontWeight: 900,
                  letterSpacing: ".3rem",
                  color: "black",
                  textDecoration: "none",
                  fontSize: 35,
                  textAlign: "center",
                  borderBottom:1
                }}
              >
                Trigger A Lambda
              </Typography>
            </Box>

            <Box sx={{ pt: 3 }}>
              <Button variant="contained" sx={{minWidth:400}}>
                <Typography>Trigger Times of India Lambda</Typography>
              </Button>
            </Box>
            <Box sx={{ pt: 3 }}>
              <Button variant="contained" sx={{minWidth:400}}>
                <Typography>Trigger CBC Lambda</Typography>
              </Button>
            </Box>
            <Box sx={{ pt: 3,pb:3 }}>
              <Button variant="contained" sx={{minWidth:400}}>
                <Typography>Trigger Government of Canada Lambda</Typography>
              </Button>
            </Box>
          </Grid>
          <Grid container direction="column" alignItems="center" sx={{borderLeft:1,borderRight:1,borderBottom:1, maxWidth:500 }}>
            <Box sx={{ pt: 3 }}>
              <Typography
                sx={{
                  fontFamily: "monospace",
                  fontWeight: 900,
                  letterSpacing: ".3rem",
                  color: "black",
                  textDecoration: "none",
                  fontSize: 35,
                  textAlign: "center",
                  borderBottom:1
                }}
              >
                Train New Data
              </Typography>
            </Box>
            <Box sx={{ pt: 3,pb:3 }}>
              <Button variant="contained" sx={{minWidth:400}}>
                <Typography>Run Model</Typography>
              </Button>
            </Box>
          </Grid>
        </Grid>
      </Grid>
    </ThemeProvider>
  );
}

export default Admin;
