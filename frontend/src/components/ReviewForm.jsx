import { useState } from "react";

export default function ReviewForm({ onSubmit, loading }) {
  const [text, setText] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (text.trim().length < 5) return;
    onSubmit(text);
    setText("");
  };

  return (
    <>
      <h2>Analyze Review</h2>
      <label className="label">Paste product review text</label>

      <form onSubmit={handleSubmit}>
        <textarea
          placeholder="Example: This product is amazing. Great quality and fast delivery."
          value={text}
          onChange={(e) => setText(e.target.value)}
        />

        <div className="row">
          <button disabled={loading}>
            {loading ? "Analyzing..." : "Analyze"}
          </button>
          <span className="mini">
            Tip: English reviews give more accurate sentiment with SST-2 model.
          </span>
        </div>
      </form>
    </>
  );
}
