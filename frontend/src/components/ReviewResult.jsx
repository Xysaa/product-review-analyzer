export default function ReviewResult({ result }) {
  if (!result) {
    return (
      <>
        <h2>Analysis Result</h2>
        <p className="mini">Submit a review to see sentiment and extracted key points.</p>
      </>
    );
  }

  const badgeClass =
    result.sentiment === "positive"
      ? "badge positive"
      : result.sentiment === "negative"
      ? "badge negative"
      : "badge neutral";

  return (
    <>
      <h2>Analysis Result</h2>

      <div className="kv">
        <span>Sentiment</span>
        <span className={badgeClass}>{result.sentiment}</span>
      </div>

      <div className="kv">
        <span>Confidence</span>
        <span>{Number(result.sentiment_score).toFixed(2)}</span>
      </div>

      <div className="split" style={{ marginTop: 12 }}>
        <div>
          <div className="label">Pros</div>
          {result.key_points?.pros?.length ? (
            <ul>
              {result.key_points.pros.map((p, i) => (
                <li key={i}>{p}</li>
              ))}
            </ul>
          ) : (
            <p className="mini">No pros detected.</p>
          )}
        </div>

        <div>
          <div className="label">Cons</div>
          {result.key_points?.cons?.length ? (
            <ul>
              {result.key_points.cons.map((c, i) => (
                <li key={i}>{c}</li>
              ))}
            </ul>
          ) : (
            <p className="mini">No cons detected.</p>
          )}
        </div>
      </div>

      <div style={{ marginTop: 12 }}>
        <div className="label">Summary</div>
        <div className="kv" style={{ justifyContent: "flex-start" }}>
          {result.key_points?.summary || "-"}
        </div>
      </div>
    </>
  );
}
