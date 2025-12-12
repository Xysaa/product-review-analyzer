import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:6543",
  headers: {
    "Content-Type": "application/json",
  },
});

export const analyzeReview = (reviewText) =>
  api.post("/api/analyze-review", {
    review_text: reviewText,
  });

export const getReviews = () =>
  api.get("/api/reviews");
