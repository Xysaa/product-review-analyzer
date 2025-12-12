import { useEffect, useState } from "react";
import { analyzeReview, getReviews } from "./api/reviewApi";
import ReviewForm from "./components/ReviewForm";
import ReviewResult from "./components/ReviewResult";
import ReviewList from "./components/ReviewList";

export default function App() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [reviews, setReviews] = useState([]);
  const [error, setError] = useState("");

  const loadReviews = async () => {
    const res = await getReviews();
    setReviews(res.data.items || []);
  };

  const handleAnalyze = async (text) => {
    try {
      setLoading(true);
      setError("");
      const res = await analyzeReview(text);
      setResult(res.data);
      await loadReviews();
    } catch (e) {
      setError(e?.response?.data?.error || "Failed to analyze review");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadReviews();
  }, []);

  return (
    <div className="container">
      <div className="header">
        <div>
          <h1>Product Review Analyzer</h1>
          <p>Sentiment (Hugging Face) + Key Points (Gemini) + PostgreSQL history</p>
        </div>
        <p className="mini">Backend: http://localhost:6543</p>
      </div>

      <div className="grid">
        <div className="card">
          <ReviewForm onSubmit={handleAnalyze} loading={loading} />
          {error && <div className="error">{error}</div>}
        </div>

        <div className="card">
          <ReviewResult result={result} />
        </div>
      </div>

      <div style={{ height: 18 }} />

      <div className="card">
        <ReviewList reviews={reviews} />
      </div>
    </div>
  );
}
