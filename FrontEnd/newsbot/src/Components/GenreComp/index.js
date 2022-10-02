import { Button, Typography, Divider } from "@mui/material";
import { Box } from "@mui/material";
import React, { useEffect } from "react";
import axios from "axios";
import Modal from "@mui/material/Modal";
import { useState } from "react";
import DialogComp from "../DialogComp";

const style = {
  position: "absolute",
  top: "50%",
  left: "50%",
  transform: "translate(-50%, -50%)",
  width: 400,
  bgcolor: "background.paper",
  border: "2px solid #000",
  boxShadow: 24,
  p: 4,
};

function GenreComp(props) {
  const [open, setOpen] = React.useState(false);
  const [loading, setLoading] = useState(0);
  const handleClose = () => setOpen(false);

  var api2Response = [
    {
      title: "ss",
      description: "s",
      date: "sx",
    },
  ];

  const handleOpen = async (e) => {
    var data = JSON.stringify({
      text: props.text,
      session_id: "1234",
    });

    var config = {
      method: "post",
      url: "http://34.231.244.174/get_response_2",
      headers: {
        "Content-Type": "application/json",
      },
      data: data,
    };

    console.log("data", data);

    await axios(config)
      .then(function(response) {
        console.log(JSON.stringify(response));
        api2Response = response.data.data_to_display;
      })
      .catch(function(error) {
        console.log(error);
      });
      console.log("data", api2Response);
    setOpen(true);
  };

  return (
    <Box sx={{ pt: 0.2, pr: 0.2 }}>
      <Button onClick={handleOpen} variant="contained">
        {props.text}
      </Button>
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style}>
          <Typography
            id="modal-modal-title"
            variant="h5"
            component="h2"
            sx={{ mb: 2 }}
            color="text.secondary"
          >
            Articles Related to {props.text}:
          </Typography>
          <Divider />
          {api2Response.map((myVar) => {
            return (
              <DialogComp
                title={myVar.title}
                description={myVar.description}
                date={myVar.readable_time}
              />
            );
          })}
        </Box>
      </Modal>
    </Box>
  );
}

export default GenreComp;
