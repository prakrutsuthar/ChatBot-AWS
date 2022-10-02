import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';

export default function NavbarComp() {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar>
          <Button color="inherit" sx={{flexGrow: 1}}>
          <Typography
              variant="h3"
              noWrap
              component="div"
              href="/"
              sx={{
                ml: 75,
                display: { xs: "none", md: "flex" },
                fontFamily: "monospace",
                fontWeight: 700,
                letterSpacing: ".3rem",
                color: "inherit",
                textDecoration: "none",
                flexGrow: 1,
              }}
            >
              NewsBot
            </Typography>
            </Button>
          <Button color="inherit">Admin</Button>
        </Toolbar>
      </AppBar>
    </Box>
  );
}
