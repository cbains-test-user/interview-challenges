FROM golang:1.23.3 AS build

RUN useradd -u 1001 nonroot
WORKDIR /app
COPY go.mod ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o go-web-server .

FROM scratch
COPY --from=build /etc/passwd /etc/passwd
COPY --from=build /app/go-web-server /go-web-server
USER nonroot

EXPOSE 8080
CMD ["./go-web-server"]
