-- CreateTable
CREATE TABLE "TrendingMusic" (
    "id" SERIAL NOT NULL,
    "author" TEXT,
    "data_id" INTEGER,

    CONSTRAINT "TrendingMusic_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "TrendingData" (
    "id" SERIAL NOT NULL,
    "hashtag" VARCHAR(64) NOT NULL,
    "postAuthorNickname" VARCHAR NOT NULL,
    "description" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) DEFAULT CURRENT_TIMESTAMP,
    "deletedAt" TIMESTAMP(3),

    CONSTRAINT "TrendingData_pkey" PRIMARY KEY ("id")
);

-- AddForeignKey
ALTER TABLE "TrendingMusic" ADD CONSTRAINT "TrendingMusic_data_id_fkey" FOREIGN KEY ("data_id") REFERENCES "TrendingData"("id") ON DELETE SET NULL ON UPDATE CASCADE;
