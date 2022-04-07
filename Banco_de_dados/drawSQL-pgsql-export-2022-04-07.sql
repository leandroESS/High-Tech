CREATE TABLE "Inquilino"(
    "codIn" INTEGER NOT NULL,
    "cel" VARCHAR(255) NOT NULL,
    "endAtual" VARCHAR(255) NOT NULL,
    "nome" VARCHAR(255) NOT NULL,
    "dataNasc" DATE NOT NULL,
    "sexo" CHAR(255) NULL
);
ALTER TABLE
    "Inquilino" ADD PRIMARY KEY("codIn");
ALTER TABLE
    "Inquilino" ADD CONSTRAINT "inquilino_cel_unique" UNIQUE("cel");
CREATE TABLE "Contrato"(
    "idCont" INTEGER NOT NULL,
    "data" DATE NOT NULL,
    "descrição" VARCHAR(255) NOT NULL,
    "Empresa" INTEGER NOT NULL,
    "período" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Contrato" ADD PRIMARY KEY("idCont");
CREATE TABLE "Corretor"(
    "codCorr" INTEGER NOT NULL,
    "nome" VARCHAR(255) NOT NULL,
    "endereço" VARCHAR(255) NOT NULL,
    "cel" INTEGER NOT NULL,
    "dataNasc" DATE NOT NULL
);
ALTER TABLE
    "Corretor" ADD PRIMARY KEY("codCorr");
ALTER TABLE
    "Corretor" ADD CONSTRAINT "corretor_cel_unique" UNIQUE("cel");
CREATE TABLE "aluguel"(
    "codIn" INTEGER NOT NULL,
    "idCont" INTEGER NOT NULL,
    "codCorr" INTEGER NOT NULL,
    "idImov" INTEGER NOT NULL
);
ALTER TABLE
    "aluguel" ADD CONSTRAINT "aluguel_codin_unique" UNIQUE("codIn");
ALTER TABLE
    "aluguel" ADD CONSTRAINT "aluguel_idcont_unique" UNIQUE("idCont");
ALTER TABLE
    "aluguel" ADD CONSTRAINT "aluguel_codcorr_unique" UNIQUE("codCorr");
ALTER TABLE
    "aluguel" ADD CONSTRAINT "aluguel_idimov_unique" UNIQUE("idImov");
CREATE TABLE "Imóvel"(
    "idIMov" INTEGER NOT NULL,
    "descrição" VARCHAR(255) NOT NULL,
    "endereço" VARCHAR(255) NOT NULL,
    "preço" DOUBLE PRECISION NOT NULL,
    "idPro" INTEGER NOT NULL
);
ALTER TABLE
    "Imóvel" ADD PRIMARY KEY("idIMov");
CREATE TABLE "Proprietário"(
    "idPro" INTEGER NOT NULL,
    "nome" VARCHAR(255) NOT NULL,
    "cel" INTEGER NOT NULL,
    "endereço" INTEGER NOT NULL,
    "dataNasc" INTEGER NOT NULL
);
ALTER TABLE
    "Proprietário" ADD PRIMARY KEY("idPro");
ALTER TABLE
    "Proprietário" ADD CONSTRAINT "proprietário_cel_unique" UNIQUE("cel");
ALTER TABLE
    "aluguel" ADD CONSTRAINT "aluguel_codcorr_foreign" FOREIGN KEY("codCorr") REFERENCES "Corretor"("codCorr");
ALTER TABLE
    "aluguel" ADD CONSTRAINT "aluguel_codin_foreign" FOREIGN KEY("codIn") REFERENCES "Inquilino"("codIn");
ALTER TABLE
    "aluguel" ADD CONSTRAINT "aluguel_idcont_foreign" FOREIGN KEY("idCont") REFERENCES "Contrato"("idCont");
ALTER TABLE
    "aluguel" ADD CONSTRAINT "aluguel_idimov_foreign" FOREIGN KEY("idImov") REFERENCES "Imóvel"("idIMov");
ALTER TABLE
    "Imóvel" ADD CONSTRAINT "imóvel_idpro_foreign" FOREIGN KEY("idPro") REFERENCES "Proprietário"("idPro");