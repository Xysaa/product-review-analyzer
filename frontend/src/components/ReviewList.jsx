export default function ReviewList({ reviews }) {
  return (
    <div>
      <h2>Review History</h2>
      <p className="mini">Saved results from PostgreSQL.</p>

      {reviews.length === 0 && <p className="mini">No reviews yet.</p>}

      {reviews.map((r) => {
        const badgeClass =
          r.sentiment === "positive"
            ? "badge positive"
            : r.sentiment === "negative"
            ? "badge negative"
            : "badge neutral";

        return (
          <div key={r.id} className="historyItem">
            <div className="top">
              <div>
                <div className="small">#{r.id}</div>
                <div style={{ marginTop: 6 }}>{r.review_text}</div>
              </div>
              <span className={badgeClass}>{r.sentiment}</span>
            </div>
          </div>
        );
      })}
    </div>
  );
}
