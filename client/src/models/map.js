import axios from "axios";

const baseURL = "/api/map/";

export default {
  getMap() {
    return axios.get(baseURL);
  }
};