# =========================
# 0. 환경 변수 로드
# =========================
from dotenv import load_dotenv
import os

load_dotenv(override=True, dotenv_path="../.env")

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

PINECONE_INDEX_NAME = "wine-review2"
PINECONE_NAMESPACE = "wine-review2-namespace"


# =========================
# 1. 문서 로드 (CSV)
# =========================
from langchain_community.document_loaders import CSVLoader

loader = CSVLoader("./wine_reviews/winemag-data-130k-v2.csv")
docs = loader.load()

print(f"원본 문서 수: {len(docs)}")


# =========================
# 2. 문서 분할
# =========================
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100,
    length_function=len,
    separators=["\n\n", "\n", " ", ""]
)

chunks = text_splitter.split_documents(docs)
print(f"분할된 chunk 수: {len(chunks)}")


# =========================
# 3. Pinecone Embeddings (핵심 수정)
# =========================
from langchain_pinecone import PineconeEmbeddings

embeddings = PineconeEmbeddings(
    model="llama-text-embed-v2"
)


# =========================
# 4. Pinecone Vector Store 업로드
# =========================
from langchain_pinecone import PineconeVectorStore

BATCH_SIZE = 500  # Pinecone 권장 범위

for i in range(0, len(chunks), BATCH_SIZE):
    batch_docs = chunks[i:i + BATCH_SIZE]

    if i == 0:
        vector_store = PineconeVectorStore.from_documents(
            documents=batch_docs,
            embedding=embeddings,
            index_name=PINECONE_INDEX_NAME,
            namespace=PINECONE_NAMESPACE,
        )
    else:
        vector_store.add_documents(batch_docs)

    print(f"배치 {i // BATCH_SIZE + 1} 완료: {len(batch_docs)}개 업로드")


print("✅ 모든 문서 업로드 완료")
